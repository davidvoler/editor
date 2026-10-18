from models.context import PromptsContext
from models.module import Module
from models.prompts import (
    PromptActionType,
    PromptOption,
    PromptRequest,
    PromptResponse,
    PromptRouterType,
    PromptType,
)
from models.word import WordTranslation
from prompts.video_extract import extract_from_part
from utils.context_utils import get_or_create_context, save_context
from utils.course_utils import get_course
from utils.module_utils import create_module, get_course_modules
from utils.prompt_utils import save_prompt_response
from utils.video_utils import (
    VideoError,
    count_parts,
    create_parts,
    fetch_subtitles,
    find_video_url,
    get_module_video,
    mark_part_extracted,
    next_part_to_extract,
    part_counts,
    save_sentences,
    save_video,
    video_title,
)
from utils.words_utils import save_words


def _minutes(seconds: int) -> str:
    return f"{seconds // 60} minutes" if seconds % 60 == 0 else f"{seconds} seconds"


def split_options(course_id: int, module_id: int, subtitles) -> list[PromptOption]:
    """One option per offered part length, e.g. "Break into 4 parts of 3 minutes"."""
    return [
        PromptOption(
            course_id=course_id, module_id=module_id,
            option_text=f"Break into {count} parts of {_minutes(length)}",
            router_type=PromptRouterType.VIDEO, prompt_type=PromptType.VIDEO_PARTS,
            prompt_values=[length], is_option=True,
        )
        for length, count in part_counts(subtitles)
    ]


def extract_option(course_id: int, module_id: int, part_title: str) -> PromptOption:
    return PromptOption(
        course_id=course_id, module_id=module_id,
        option_text=f"Extract words and sentences from {part_title}",
        router_type=PromptRouterType.VIDEO, prompt_type=PromptType.VIDEO_EXTRACT, is_option=True,
    )


def _response(prompt_request: PromptRequest, prompt_type: PromptType, message: str, *,
              course_id: int, module_id: int = 0, lesson_id: int = 0,
              options: list[PromptOption] | None = None, results: dict | None = None,
              action: PromptActionType = PromptActionType.SIMPLE) -> PromptResponse:
    return PromptResponse(
        request_user_message=prompt_request.user_message,
        course_id=course_id, module_id=module_id, lesson_id=lesson_id,
        option=options, results=results or {}, ui_chat_response={"message": message},
        prompt_router_type=PromptRouterType.VIDEO, prompt_type=prompt_type, prompt_action_type=action,
    )


async def _start_video_module(prompt_request: PromptRequest) -> PromptResponse:
    """Creates a module for the video in the message and offers how to split it."""
    course = await get_course(prompt_request.course_id)
    url = find_video_url(prompt_request.user_message)
    try:
        subtitles = fetch_subtitles(url or "", course.lang)
    except VideoError as error:
        return _response(prompt_request, PromptType.VIDEO_MODULE, str(error), course_id=course.course_id)
    count = len(await get_course_modules(course.course_id))
    title = await video_title(url) or f"Video module {count + 1}"
    module = await create_module(Module(course_id=course.course_id, title=title[:255], weight=count))
    await save_video(course.course_id, module.module_id, course.lang, url, subtitles)
    # The module becomes current with no lesson yet; its parts become its lessons.
    await save_context(PromptsContext(course_id=course.course_id, module_id=module.module_id, lesson_id=0))
    response = _response(
        prompt_request, PromptType.VIDEO_MODULE,
        f'Created the module "{module.title}". How should the video be split?',
        course_id=course.course_id, module_id=module.module_id,
        options=split_options(course.course_id, module.module_id, subtitles),
    )
    await save_prompt_response(response)
    return response


async def _split_into_parts(prompt_request: PromptRequest) -> PromptResponse:
    """Creates one lesson per part of the module's video."""
    context = await get_or_create_context(prompt_request.course_id)
    course_id, module_id = context.course_id, context.module_id
    video = await get_module_video(module_id)
    if not video:
        return _response(prompt_request, PromptType.VIDEO_PARTS, "This module has no video.", course_id=course_id)
    parts, _ = await count_parts(module_id)
    if parts:
        return _response(prompt_request, PromptType.VIDEO_PARTS, "The video is already split into parts.",
                         course_id=course_id, module_id=module_id)
    seconds = int((prompt_request.prompt_values or [180])[0])
    lessons = await create_parts(course_id, module_id, video[1], seconds)
    await save_context(PromptsContext(course_id=course_id, module_id=module_id, lesson_id=lessons[0].lesson_id))
    response = _response(
        prompt_request, PromptType.VIDEO_PARTS, f"Split the video into {len(lessons)} parts.",
        course_id=course_id, module_id=module_id, lesson_id=lessons[0].lesson_id,
        results={"parts": [{"part": l.title, "text": (l.description or "")[:120] + "..."} for l in lessons]},
        options=[extract_option(course_id, module_id, lessons[0].title)],
    )
    await save_prompt_response(response)
    return response


async def _extract_next_part(prompt_request: PromptRequest) -> PromptResponse:
    """Extracts words and sentences from the first part not extracted yet."""
    context = await get_or_create_context(prompt_request.course_id)
    course_id, module_id = context.course_id, context.module_id
    part = await next_part_to_extract(module_id)
    if not part:
        return _response(prompt_request, PromptType.VIDEO_EXTRACT, "All parts are already extracted.",
                         course_id=course_id, module_id=module_id)
    course = await get_course(course_id)
    extract = await extract_from_part(
        part.description, lang=course.lang, to_lang=course.to_lang, level=course.level,
        provider=prompt_request.provider, model=prompt_request.model,
    )
    words = [w for w in extract.words if w.word.strip()]
    await save_words(lang=course.lang, to_lang=course.to_lang, course_id=course_id, module_id=module_id,
                     words=[WordTranslation(word=w.word.strip(), translation=w.translation) for w in words])
    await save_sentences(course.lang, course_id, module_id, part.lesson_id,
                         [(s.sentence, s.translation) for s in extract.sentences if s.sentence.strip()])
    await mark_part_extracted(part.lesson_id, [w.word.strip() for w in words])
    # The part becomes current, so its exercises go into it.
    await save_context(PromptsContext(course_id=course_id, module_id=module_id, lesson_id=part.lesson_id))
    parts, extracted = await count_parts(module_id)
    next_part = await next_part_to_extract(module_id)
    response = _response(
        prompt_request, PromptType.VIDEO_EXTRACT,
        f"Extracted {len(words)} words and {len(extract.sentences)} sentences from {part.title} "
        f"({extracted} of {parts} parts done).",
        course_id=course_id, module_id=module_id, lesson_id=part.lesson_id,
        results={
            "words": [{"word": w.word, "translation": w.translation} for w in words],
            "sentences": [{"sentence": s.sentence, "translation": s.translation} for s in extract.sentences],
        },
        options=[extract_option(course_id, module_id, next_part.title)] if next_part else None,
        action=PromptActionType.ASK_AI,
    )
    await save_prompt_response(response)
    return response


async def handle_prompt_video_request(prompt_request: PromptRequest) -> PromptResponse:
    match prompt_request.prompt_type:
        case PromptType.VIDEO_PARTS:
            return await _split_into_parts(prompt_request)
        case PromptType.VIDEO_EXTRACT:
            return await _extract_next_part(prompt_request)
        case _:
            return await _start_video_module(prompt_request)
