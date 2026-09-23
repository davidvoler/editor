from pydantic import BaseModel, Field
from enum import Enum
from prompt_router.router import PromptType, PromptRequest
from prompts.single_choice import SingleChoicePrompt





async def identify_lesson_type(prompt_request: PromptRequest) -> LessonType:
    # Implement the logic to identify the lesson type based on the prompt request
    return LessonType.SINGLE_CHOICE

from models.prompts_old import (
    PromptRequest,
    PromptOption,
    PromptContext,
    PromptActionType,
    LessonType,
    PromptResponse
)   



from utils.prompt_utils import save_prompt_request


async def _identify_prompt_type(prompt_request: PromptRequest) -> LessonType:
    # Implement the logic to identify the prompt type based on the user message and context
    pass

async def _process_prompt_request(prompt_request: PromptRequest, lesson_type: LessonType) -> PromptResponse:
    # Implement the logic to process the prompt request based on the identified lesson type
    match(lesson_type):
        case LessonType.MULTIPLE_CHOICE:
            # Handle multiple choice lesson logic
            pass
        case LessonType.FILL_IN_THE_BLANK:
            # Handle fill in the blank lesson logic
            pass
        case LessonType.TRUE_FALSE:
            # Handle true/false lesson logic
            pass
        case LessonType.SINGLE_CHOICE:
            # Handle single choice lesson logic
            pass
        case LessonType.EXPLANATION:
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








