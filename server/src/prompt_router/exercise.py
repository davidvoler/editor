from pydantic import BaseModel, Field
from enum import Enum
from prompt_router.router import PromptType, PromptRequest
from prompts.single_choice import SingleChoicePrompt

class ExerciseType(Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    FILL_IN_THE_BLANK = "fill_in_the_blank"
    TRUE_FALSE = "true_false"
    SINGLE_CHOICE = "single_choice"
    EXPLANATION = "explanation"






async def identify_exercise_type(prompt_request: PromptRequest) -> ExerciseType:
    # Implement the logic to identify the exercise type based on the prompt request
    return ExerciseType.SINGLE_CHOICE

async def create_exercise(prompt_request: PromptRequest):
    exercise_type = await identify_exercise_type(prompt_request)
    if exercise_type == ExerciseType.SINGLE_CHOICE:
        single_choice_prompt = SingleChoicePrompt(prompt_request)
        question, answer = await single_choice_prompt.generate()
        return [Exercise(question=question, answer=answer)]
    # Implement logic for other exercise types as needed
    return []