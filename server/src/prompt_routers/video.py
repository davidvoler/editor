from pydantic import BaseModel, Field
from enum import Enum
from prompt_router.router import PromptType, PromptRequest
from prompts.single_choice import SingleChoicePrompt





async def identify_video_type(prompt_request: PromptRequest) -> VideoType:
    # Implement the logic to identify the video type based on the prompt request
    return VideoType.SINGLE_CHOICE

from models.prompts_old import (
    PromptRequest,
    PromptOption,
    PromptContext,
    PromptActionType,
    PromptResponse,
    VideoPromptType,
    PromptResponse,
)   



from utils.prompt_utils import save_prompt_request
async def _identify_prompt_type(prompt_request: PromptRequest) -> VideoPromptType:
    # Implement the logic to identify the prompt type based on the user message and context
    pass


async def _process_prompt_request(prompt_request: PromptRequest, video_type: VideoPromptType) -> PromptResponse:
    # Implement the logic to process the prompt request based on the identified video type
    match(video_type):
        case VideoPromptType.SECTIONS:
            # Handle sections video logic
            pass
        case VideoPromptType.PARTS:
            # Handle parts video logic
            pass
        case _:
            # Handle unknown prompt type
            pass



async def _offer_options(prompt_request: PromptRequest) -> list[PromptOption]:
    # Implement the logic to offer options to the user based on the prompt request
    pass


async def handle_prompt_video_request(prompt_request: PromptRequest) -> PromptResponse:
    video_type = await _identify_prompt_type(prompt_request)
    # Implement the logic to handle the prompt request based on the identified prompt type
    if not video_type:
        return await _offer_options(prompt_request)
    else:
        return await _process_prompt_request(prompt_request, video_type)








