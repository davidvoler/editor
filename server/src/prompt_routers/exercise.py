from models.prompts import (
    PromptRequest,
    PromptOption,
    PromptContext,
    ExerciseType,
    PromptActionType,
    PromptResponse,
)   
from utils.prompt_utils import save_prompt_request


from utils.prompt_utils import save_prompt_request
async def _identify_prompt_type(prompt_request: PromptRequest) -> ExerciseType:
    # Implement the logic to identify the prompt type based on the user message and context
    pass


async def _process_prompt_request(prompt_request: PromptRequest, exercise_type: ExerciseType) -> PromptResponse:
    # Implement the logic to process the prompt request based on the identified exercise type
    match(exercise_type):
        case ExerciseType.MULTIPLE_CHOICE:
            # Handle multiple choice exercise logic
            pass
        case ExerciseType.FILL_IN_THE_BLANK:
            # Handle fill in the blank exercise logic
            pass
        case ExerciseType.TRUE_FALSE:
            # Handle true/false exercise logic
            pass
        case ExerciseType.SINGLE_CHOICE:
            # Handle single choice exercise logic
            pass
        case ExerciseType.EXPLANATION:
            # Handle explanation exercise logic
            pass
        case _:
            # Handle unknown prompt type
            pass



async def _offer_options(prompt_request: PromptRequest) -> PromptResponse:
    # Implement the logic to offer options to the user based on the prompt request
    pass


async def handle_prompt_exercise_request(prompt_request: PromptRequest) -> PromptResponse:
    exercise_type = await _identify_prompt_type(prompt_request)
    # Implement the logic to handle the prompt request based on the identified prompt type
    if not exercise_type:
        save_prompt_request(prompt_request, PromptActionType.OPTIONS)
        return await _offer_options(prompt_request)
    else:
        save_prompt_request(prompt_request, PromptActionType.ASK_AI)
        await _process_prompt_request(prompt_request, exercise_type)








