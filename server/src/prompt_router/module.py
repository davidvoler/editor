from pydantic import BaseModel, Field
from enum import Enum
from prompt_router.router import PromptType, PromptRequest
from prompts.single_choice import SingleChoicePrompt




class ModulePromptsOptions(BaseModel):
    pass


class  Module(BaseModel):
    question: str = Field(..., description="The question for the exercise.")
    answer: str = Field(..., description="The answer for the exercise.")


async def identify_exercise_type(prompt_request: PromptRequest) ->  ModuleType:
    # Implement the logic to identify the exercise type based on the prompt request
    return  ModuleType.SINGLE_CHOICE

async def create_exercise(prompt_request: PromptRequest) -> list[ Module]:
    exercise_type = await identify_exercise_type(prompt_request)
    if exercise_type ==  ModuleType.SINGLE_CHOICE:
        single_choice_prompt = SingleChoicePrompt(prompt_request)
        question, answer = await single_choice_prompt.generate()
        return [ Module(question=question, answer=answer)]
    # Implement logic for other exercise types as needed
    return []