from models.prompts import (
    PromptRequest,
    PromptRouterType,
    PromptResponse
) 

from prompt_routers.course import handle_prompt_course_request
from prompt_routers.module import handle_prompt_module_request
from prompt_routers.lesson import handle_prompt_lesson_request
from prompt_routers.exercise import handle_prompt_exercise_request
from prompt_routers.vocabulary import handle_prompt_vocabulary_request


async def _identify_prompt_type(prompt_request: PromptRequest) -> PromptRouterType:
    # Implement the logic to identify the prompt type based on the user message and context
    # TODO: temporary hardcode to test the task pipeline end-to-end
    return PromptRouterType.COURSE


async def _process_prompt_request(prompt_request: PromptRequest, prompt_type: PromptRouterType) -> PromptResponse:
    # Implement the logic to process the prompt request based on the identified prompt type
    match(prompt_type):
        case PromptRouterType.COURSE:
            # Handle create course logic
            return await handle_prompt_course_request(prompt_request)
        case PromptRouterType.MODULE:
            # Handle create module logic
            return await handle_prompt_module_request(prompt_request)
        case PromptRouterType.LESSON:
            # Handle create lesson logic
            return await handle_prompt_lesson_request(prompt_request)
        case PromptRouterType.VOCABULARY:
            # Handle vocabulary logic
            return await handle_prompt_vocabulary_request(prompt_request)
        case PromptRouterType.EXERCISE:
            # Handle exercise logic
            return await handle_prompt_exercise_request(prompt_request)
        case _:
            # Handle unknown prompt type
            raise ValueError(f"Unknown prompt type: {prompt_type}")



async def _offer_options(prompt_request: PromptRequest) -> PromptResponse:
    # Implement the logic to offer options to the user based on the prompt request
    pass


async def handle_prompt_request(prompt_request: PromptRequest) -> PromptResponse:
    prompt_router_type = await _identify_prompt_type(prompt_request)
    if prompt_router_type:
        response = await _process_prompt_request(prompt_request, prompt_router_type)
        if response:
            return response
    return await _offer_options(prompt_request)






