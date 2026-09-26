from pydantic import BaseModel, Field
from enum import Enum
from prompts.single_choice import get_single_choice
from models.prompts import PromptRequest, PromptType, PromptResponse



async def identify_lesson_type(prompt_request: PromptRequest) -> PromptType:
    # Implement the logic to identify the lesson type based on the prompt request
    return PromptType.LESSON_CREATE




from utils.prompt_utils import save_prompt_request


async def _identify_prompt_type(prompt_request: PromptRequest) -> PromptType:
    # Implement the logic to identify the prompt type based on the user message and context
    pass

async def _process_prompt_request(prompt_request: PromptRequest, lesson_type: PromptType) -> PromptResponse:
    # Implement the logic to process the prompt request based on the identified lesson type
    match(lesson_type):
        case PromptType.MULTIPLE_CHOICE:
            # Handle multiple choice lesson logic
            pass
        case PromptType.FILL_IN_THE_BLANK:
            # Handle fill in the blank lesson logic
            pass
        case PromptType.TRUE_FALSE:
            # Handle true/false lesson logic
            pass
        case PromptType.SINGLE_CHOICE:
            # Handle single choice lesson logic
            return await get_single_choice(prompt_request)
        case PromptType.EXPLANATION:
            # Handle explanation lesson logic
            pass
        case _:
            # Handle unknown prompt type
            pass



async def _offer_options(prompt_request: PromptRequest) -> PromptResponse:
    # Implement the logic to offer options to the user based on the prompt request
    pass


async def handle_prompt_lesson_request(prompt_request: PromptRequest) ->PromptResponse:
    lesson_type = await _identify_prompt_type(prompt_request)
    # Implement the logic to handle the prompt request based on the identified prompt type
    if not lesson_type:
        return await _offer_options(prompt_request)
    else:
        await _process_prompt_request(prompt_request, lesson_type)








