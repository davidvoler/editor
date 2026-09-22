from models.prompts import (
    PromptRequest,
    PromptRouterType,
    PromptOption,
    PromptContext,
    PromptActionType,
)



def _save_prompt_request(prompt_request: PromptRequest, action: PromptActionType, details:dict) -> None:
    """
    Save the prompt request to a database or storage.
    Args:
        prompt_request (PromptRequest): The prompt request to be saved.
        action (PromptActionType): The action associated with the prompt request.
        details (dict): Additional details related to the prompt request.
    Returns:
        None
    """
    pass