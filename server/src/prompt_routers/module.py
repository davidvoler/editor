from utils.module_utils import create_module
from models.module import Module

from models.prompts import (
    PromptRequest,
    PromptResponse,
    PromptType,
    PromptRouterType
)   
from prompt_routers.vocabulary import handle_prompt_vocabulary_request

from utils.prompt_utils import save_prompt_request
async def _identify_prompt_type(prompt_request: PromptRequest) -> PromptType:
    # Implement the logic to identify the prompt type based on the user message and context
    pass

async def suggest_options(prompt_request: PromptRequest) -> PromptResponse:
    # Implement the logic to suggest options to the user based on the prompt request
    pass



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
            return m
        case PromptType.MODULE_CREATE_SUGGEST_WORDS:
            # Handle module create suggest words logic
            m = await _create_module(prompt_request)
            prompt_request.module_id = m.module_id
            prompt_request.prompt_router = PromptRouterType.VOCABULARY
            prompt_request.prompt_type = PromptType.VOCABULARY_SUGGEST_WORDS
            return await handle_prompt_vocabulary_request(prompt_request)
        case PromptType.MODULE_ATTRIBUTES:
            # Handle module attributes logic
            pass
        case _:
            # Handle unknown prompt type
            pass
    return await suggest_options(prompt_request)


async def _offer_options(prompt_request: PromptRequest) -> PromptResponse:
    # Implement the logic to offer options to the user based on the prompt request
    pass


async def handle_prompt_module_request(prompt_request: PromptRequest) -> PromptResponse:
    prompt_type = await _identify_prompt_type(prompt_request)
    # Implement the logic to handle the prompt request based on the identified prompt type
    if not prompt_type:

        return await _offer_options(prompt_request)
    else:
        return await _process_prompt_request(prompt_request, prompt_type)








