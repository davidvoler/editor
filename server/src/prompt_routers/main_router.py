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


async def _identify_prompt_router_type(prompt_request: PromptRequest) -> PromptRouterType:
    if prompt_request.last_router_type and prompt_request.last_router_type != PromptRouterType.UNKNOWN:
        return prompt_request.last_router_type
    if prompt_request.course_id is None or prompt_request.course_id<=0:
        # We do not have a course yet
        return PromptRouterType.COURSE
    if prompt_request.module_id is None or prompt_request.module_id<=0:
        # We do not have a module yet
        return PromptRouterType.MODULE
    # do we have enough words?
    if prompt_request.unused_words() <=2:
        return PromptRouterType.VOCABULARY
    if prompt_request.words_count() >= 1:
        return PromptRouterType.EXERCISE
    

async def _process_prompt_request(prompt_request: PromptRequest, prompt_router_type: PromptRouterType) -> PromptResponse:
    # Implement the logic to process the prompt request based on the identified prompt type
    match(prompt_router_type):
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
            return None


async def _offer_options(prompt_request: PromptRequest) -> PromptResponse:
    # Implement the logic to offer options to the user based on the prompt request
    pass

async def handle_prompt_request(prompt_request: PromptRequest) -> PromptResponse:
    if not prompt_request.router_type or prompt_request.router_type == PromptRouterType.UNKNOWN:
        prompt_router_type = await _identify_prompt_router_type(prompt_request)
    else:
        prompt_router_type = prompt_request.router_type
    if prompt_router_type:
        response = await _process_prompt_request(prompt_request, prompt_router_type)
        if response:
            return response
    return await _offer_options(prompt_request)






