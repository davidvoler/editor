from models.exercise import Exercise
from models.prompts import (
    PromptRequest,
    PromptActionType,
    PromptResponse,
    PromptRouterType,
    PromptType,
)
from prompts.single_choice import get_single_choice_for_words
from utils.context_options import context_stats, EXERCISES_PER_REQUEST, MAX_EXERCISES_PER_LESSON
from utils.course_utils import get_course
from utils.exercise_utils import create_exercise
from utils.prompt_utils import save_prompt_response


async def _create_single_choice(prompt_request: PromptRequest) -> PromptResponse:
    """Turns the module's unused words into single-choice exercises in the current lesson."""
    stats = await context_stats(prompt_request.course_id)
    context = stats.context
    count = min(EXERCISES_PER_REQUEST, MAX_EXERCISES_PER_LESSON - stats.lesson_exercises)
    words = stats.unused_words[:max(count, 0)]
    created = []
    if words:
        course = await get_course(context.course_id)
        generated = await get_single_choice_for_words(
            words, lang=course.lang, to_lang=course.to_lang, level=course.level,
            provider=prompt_request.provider, model=prompt_request.model,
        )
        # Keep one question per requested word; the model may repeat or invent words.
        by_word = {e.word.strip().lower(): e for e in generated.exercises}
        for word in words:
            e = by_word.get(word.lower())
            if not e:
                continue
            created.append(await create_exercise(Exercise(
                course_id=context.course_id, module_id=context.module_id, lesson_id=context.lesson_id,
                exercise_type=PromptType.EXERCISE_SINGLE_CHOICE.value, word=word,
                question=e.sentence, answer=word, options={"incorrect": e.incorrect_options[:3]},
                sentence_alt1=e.translation,
            )))
    message = (f"Created {len(created)} exercises." if created
               else "There are no unused words to make exercises for." if not words
               else "The AI did not return usable exercises; try again.")
    response = PromptResponse(
        request_user_message=prompt_request.user_message,
        course_id=context.course_id, module_id=context.module_id, lesson_id=context.lesson_id,
        results={"exercises": [
            {"word": e.word, "question": e.question, "answer": e.answer,
             "wrong_options": ", ".join(e.options["incorrect"]), "translation": e.sentence_alt1}
            for e in created
        ]} if created else {},
        ui_chat_response={"message": message},
        prompt_router_type=PromptRouterType.EXERCISE,
        prompt_type=PromptType.EXERCISE_SINGLE_CHOICE,
        prompt_action_type=PromptActionType.ASK_AI,
    )
    await save_prompt_response(response)
    return response


async def handle_prompt_exercise_request(prompt_request: PromptRequest) -> PromptResponse:
    # Single choice is the only exercise type the AI creates so far.
    return await _create_single_choice(prompt_request)
