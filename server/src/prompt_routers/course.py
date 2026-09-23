from models.prompts_old import (
    PromptRequest,
    PromptOption,
    PromptContext,
    PromptActionType,
    CoursePromptType,
    PromptResponseType,
    PromptResponse,
    PromptOptionData,
)
from utils.prompt_utils import save_prompt_request
from utils.course_utils import create_course
from models.course import Course


async def _identify_prompt_type(prompt_request: PromptRequest) -> CoursePromptType:
    if "create course" in prompt_request.message.lower():
        return CoursePromptType.CREATE_COURSE
    if "create" in prompt_request.message.lower() and "course"  in prompt_request.message.lower():
        return CoursePromptType.CREATE_COURSE
    if "attributes" in prompt_request.message.lower():
        return CoursePromptType.COURSE_ATTRIBUTES
    return None


def create_options(prompt_request: PromptRequest) -> list[PromptOption]:
    options = [
        PromptOption(
            label="Create a new Course",
            value="create_course"
        ),
        PromptOption(
            label="Change course attributes",
            value="course_attributes"
        ),
        PromptOption(
            label="View course details",
            value="course_missing_data",
            option_data=[
                PromptOptionData(
                    label="lang",
                    value="en"
                )
            ]
        )
    ]

async def _process_prompt_request(prompt_request: PromptRequest, course_type: CoursePromptType) -> PromptResponse:
    # Implement the logic to process the prompt request based on the identified course type
    match(course_type):
        case CoursePromptType.CREATE_COURSE:
            save_prompt_request(prompt_request, PromptActionType.SIMPLE_ACTION)
            course = Course(
                lang="en",  # Replace with actual value from prompt_request
                to_lang="fr",  # Replace with actual value from prompt_request
                user_id=1,  # Replace with actual value from prompt_request
                school="Example School",  # Replace with actual value from prompt_request
                title="Example Course",  # Replace with actual value from prompt_request
                description="Example Description",  # Replace with actual value from prompt_request
                course_options={},  # Replace with actual value from prompt_request
                status="draft"  # Replace with actual value from prompt_request
            )
            return await create_course(course)
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




