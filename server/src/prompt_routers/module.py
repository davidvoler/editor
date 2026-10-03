from utils.module_utils import create_module
from models.module import Module
from models.lesson import Lesson
from models.prompts import (
    PromptRequest,
    PromptResponse,
    PromptType,
    PromptRouterType,
    PromptActionType,
    PromptOption,
)   
from prompt_routers.vocabulary import handle_prompt_vocabulary_request
from utils.lesson_utils import create_lesson

from utils.prompt_utils import save_prompt_request
async def _identify_prompt_type(prompt_request: PromptRequest) -> PromptType:
    # Implement the logic to identify the prompt type based on the user message and context
    pass

async def _create_lesson(prompt_request: PromptRequest) -> Lesson:
    l = Lesson(
        course_id=prompt_request.course_id,
        module_id=prompt_request.module_id,
        title="Lesson 1",  # Replace with actual value from prompt_request
        content="Example lesson content",  # Replace with actual value from prompt_request
        status="draft"  # Replace with actual value from prompt_request
    )
    return await create_lesson(l)

async def _get_options(prompt_request: PromptRequest) -> list[PromptOption]:
    # Implement the logic to get options based on the prompt request
    if not prompt_request.lesson_id:
            lesson = await _create_lesson(prompt_request)
            prompt_request.lesson_id = lesson.lesson_id
    
    #do we have sufficient words 
    words = ["word1", "word2", "word3"]
    return [
        PromptOption(
            option_text=f"Create exercises for words: {words}",
            prompt_router_type=PromptRouterType.EXERCISE,
            prompt_type=PromptType.EXERCISE,
        ),
        
    ] 


async def suggest_options(prompt_request: PromptRequest) -> PromptResponse:
    # Implement the logic to suggest options to the user based on the prompt request
    return PromptResponse(
        request_user_message=prompt_request.user_message,
        course_id=prompt_request.course_id,
        module_id=prompt_request.module_id,
        lesson_id=prompt_request.lesson_id,
        option=await _get_options(prompt_request),
        prompt_router_type=PromptRouterType.MODULE,
        prompt_type=PromptType.MODULE_CREATE,
        prompt_action_type=PromptActionType.SIMPLE,
        is_option=prompt_request.is_options
    )

async def _create_module(prompt_request: PromptRequest) -> Module:
    m = Module(
        course_id=prompt_request.course_id,
        title="Module 1",  # Replace with actual value from prompt_request
        description="Example module",  # Replace with actual value from prompt_request
        status="draft"  # Replace with actual value from prompt_request
    )
    return await create_module(m)



async def _process_prompt_request(prompt_request: PromptRequest, prompt_type: PromptType) -> PromptResponse:
    # Implement the logic to process the prompt request based on the identified prompt type
    match(prompt_type):
        case PromptType.MODULE_CREATE:
            m = await _create_module(prompt_request)
            return PromptResponse(
                course_id=m.course_id,
                module_id=m.module_id,
                prompt_router_type=PromptRouterType.MODULE,
                prompt_type=PromptType.MODULE_CREATE,
                prompt_action_type=PromptActionType.SIMPLE,
                option=await _get_options(prompt_request),
                ui_chat_response=f"Module '{m.title}' created successfully.",
                is_option=prompt_request.is_options
            )
        case PromptType.MODULE_CREATE_SUGGEST_WORDS:
            # Handle module create suggest words logic
            m = await _create_module(prompt_request)
            prompt_request.module_id = m.module_id
            prompt_request.router_type = PromptRouterType.VOCABULARY
            prompt_request.prompt_type = PromptType.VOCABULARY_SUGGEST_WORDS
            return await handle_prompt_vocabulary_request(prompt_request)
        case PromptType.MODULE_ATTRIBUTES:
            # Handle module attributes logic
            pass
        case _:
            # Handle unknown prompt type
            pass
    return await suggest_options(prompt_request)



async def handle_prompt_module_request(prompt_request: PromptRequest) -> PromptResponse:
    prompt_type = await _identify_prompt_type(prompt_request)
    # Implement the logic to handle the prompt request based on the identified prompt type
    if not prompt_type:
        return await suggest_options(prompt_request)
    else:
        return await _process_prompt_request(prompt_request, prompt_type)








