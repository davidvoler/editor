from pydantic import BaseModel, Field
from enum import Enum
from prompt_router.router import PromptType, PromptRequest
from prompts.single_choice import SingleChoicePrompt





async def identify_video_type(prompt_request: PromptRequest) -> VideoType:
    # Implement the logic to identify the video type based on the prompt request
    return VideoType.SINGLE_CHOICE

from models.prompts import (
    PromptRequest,
    PromptOption,
    PromptResponse,
    PromptResponse,
    PromptType
)   



from utils.prompt_utils import save_prompt_request
async def _identify_prompt_type(prompt_request: PromptRequest) -> PromptType:
    # Implement the logic to identify the prompt type based on the user message and context
    pass


async def _suggest_options(prompt_request: PromptRequest) -> PromptResponse:
    # Implement the logic to suggest options to the user based on the prompt request
    pass

async def _process_prompt_request(prompt_request: PromptRequest, video_type: PromptType) -> PromptResponse:
    # Implement the logic to process the prompt request based on the identified video type
    match(video_type):
        case PromptType.VIDEO_SECTIONS:
            # Handle sections video logic
            pass
        case PromptType.VIDEO_PARTS:
            # Handle parts video logic
            pass
        case _:
            # Handle unknown prompt type
            pass


async def handle_prompt_video_request(prompt_request: PromptRequest) -> PromptResponse:
    video_type = await _identify_prompt_type(prompt_request)
    # Implement the logic to handle the prompt request based on the identified prompt type
    if not video_type:
        return await _suggest_options(prompt_request)
    else:
        return await _process_prompt_request(prompt_request, video_type)








