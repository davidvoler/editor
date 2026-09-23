from models.prompts_old import (
    PromptRequest,
    PromptResponse,

)   



from models.prompts_simplified import PromptType
from utils.prompt_utils import save_prompt_request
async def _identify_prompt_type(prompt_request: PromptRequest) -> PromptType:
    # Implement the logic to identify the prompt type based on the user message and context
    pass

async def suggest_options(prompt_request: PromptRequest) -> PromptResponse:
    # Implement the logic to suggest options to the user based on the prompt request
    pass


async def _process_prompt_request(prompt_request: PromptRequest, prompt_type: PromptType) -> PromptResponse:
    # Implement the logic to process the prompt request based on the identified prompt type
    match(prompt_type):
        case PromptType.MODULE_CREATE:
            # Handle create module logic
            pass
        case PromptType.MODULE_ATTRIBUTES:
            # Handle module attributes logic
            pass
        case PromptType.SUGGEST_WORDS:
            # Handle suggest words logic
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








