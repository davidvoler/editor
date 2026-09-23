from models.prompts_old import (
    PromptRequest,
    PromptOption,
    PromptContext,
    PromptActionType,
    ModulePromptType,
    PromptResponse,
)   



from utils.prompt_utils import save_prompt_request
async def _identify_prompt_type(prompt_request: PromptRequest) -> ModulePromptType:
    # Implement the logic to identify the prompt type based on the user message and context
    pass


async def _process_prompt_request(prompt_request: PromptRequest, prompt_type: ModulePromptType) -> PromptResponse:
    # Implement the logic to process the prompt request based on the identified prompt type
    match(prompt_type):
        case ModulePromptType.CREATE_MODULE:
            # Handle create module logic
            pass
        case ModulePromptType.MODULE_ATTRIBUTES:
            # Handle module attributes logic
            pass
        case ModulePromptType.SUGGEST_WORDS:
            # Handle suggest words logic
            pass
        case _:
            # Handle unknown prompt type
            pass



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








