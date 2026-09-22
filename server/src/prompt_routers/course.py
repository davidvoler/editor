from models.prompts import (
    PromptRequest,
    PromptOption,
    PromptContext,
    PromptActionType,
    CoursePromptType,
    PromptResponseType,
    PromptResponse,
)
from utils.prompt_utils import save_prompt_request



async def create_course(prompt_request: PromptRequest) -> PromptResponse:
    # Implement the logic to create a course based on the prompt request
    pass

async def _identify_prompt_type(prompt_request: PromptRequest) -> PromptActionType:
    # Implement the logic to identify the prompt type based on the user message and context
    pass



async def _process_prompt_request(prompt_request: PromptRequest, course_type: CoursePromptType) -> PromptResponse:
    # Implement the logic to process the prompt request based on the identified course type
    match(course_type):
        case CoursePromptType.CREATE_COURSE:
            save_prompt_request(prompt_request, PromptActionType.SIMPLE_ACTION)
            return await create_course(prompt_request)
        case CoursePromptType.COURSE_ATTRIBUTES:
            # Handle course attributes logic
            pass
        case _:
            # Handle unknown prompt type
            pass

async def _offer_options(prompt_request: PromptRequest) -> PromptResponse:
    # Implement the logic to offer options to the user based on the prompt request
    pass


async def handle_prompt_course_request(prompt_request: PromptRequest) -> PromptResponse:
    course_type = await _identify_prompt_type(prompt_request)
    # Implement the logic to handle the prompt request based on the identified prompt type
    if not course_type:
        return await _offer_options(prompt_request)
    else:
        return await _process_prompt_request(prompt_request, course_type)




