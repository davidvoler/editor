from unittest import case

from pydantic import BaseModel, Field
from enum import Enum


class CourseOption(BaseModel):
    extra_system_prompt: str|None = Field(..., description="Additional system prompt for all request related to the course.")
    target_language: str|None = Field(..., description="The target language for the course.")
    student_language: str|None = Field(..., description="The language spoken by the student.")
    level: str|None = Field(..., description="The level of the course.")
    target_audience: str|None = Field(..., description="The target audience for the course.")
    target_age_group: str|None = Field(..., description="The target age group for the course.")
    teaching_method: str|None = Field(..., description="The teaching method used for the course.")
    learning_objectives: str|None = Field(..., description="The learning objectives for the course.")


class ModuleOption(BaseModel):
    max_words_in_sentences: int|None = Field(..., description="The maximum number of words allowed in sentences for the module.")
    transliteration: bool|None = Field(..., description="Indicates whether transliteration is enabled for the module.")
    transliteration_format: str|None = Field(..., description="The format used for transliteration in the module.")
    number_of_exercises_per_word: int|None = Field(..., description="The number of exercises to create per word for the module.")
    exercise_type_single_choice: bool|None = Field(..., description="Indicates whether the exercise type is single choice for the module.")
    exercise_type_multiple_choice: bool|None = Field(..., description="Indicates whether the exercise type is multiple choice for the module.")
    exercise_type_fill_in_the_blank: bool|None = Field(..., description="Indicates whether the exercise type is fill in the blank for the module.")
    exercise_type_true_false: bool|None = Field(..., description="Indicates whether the exercise type is true/false for the module.")
    exercise_type_matching: bool|None = Field(..., description="Indicates whether the exercise type is matching for the module.")
    exercise_type_explanation: bool|None = Field(..., description="Indicates whether the exercise type is explanation for the module.")



class Word(BaseModel):
    text: str = Field(..., description="The word.")
    used: bool = Field(..., description="Indicates whether the word has been used.")
    taught: bool = Field(..., description="Indicates whether the word has been taught. and used to create exercises and sentences.")
    

    
class PromptType(Enum):
    CREATE_COURSE = "create_course"
    CREATE_MODULE = "create_module"
    CREATE_LESSON = "create_lesson"
    VOCABULARY = "vocabulary"
    EXERCISE = "exercise"
    

class PromptContext(BaseModel):
    course_options: CourseOption|None = Field(..., description="The course context for the prompt.")
    module_options: ModuleOption|None = Field(..., description="The module context for the prompt.")
    words_list: list[Word]|None = Field(..., description="The list of words in the context.")
    course_id: int|None = Field(..., description="The ID of the course in the context.")
    module_id: int|None = Field(..., description="The ID of the module in the context.")
    lesson_id: int|None = Field(..., description="The ID of the lesson in the context.")

class PromptOption(BaseModel):
    option_text: str = Field(..., description="The text of the option.")
    option_value: str = Field(..., description="The value associated with the option.")
    prompt_type: PromptType = Field(..., description="The type of prompt this option is associated with.")
    


class PromptRequest(BaseModel):
    user_message: str = Field(..., description="The message input from the user.") 
    context: PromptContext|None = Field(..., description="The context for the prompt, including course, module, and words.")
    provider: str = Field(..., description="The AI provider associated with the prompt request.")
    model: str = Field(..., description="The model to use for the prompt request.")



async def identify_prompt_type(prompt_request: PromptRequest) -> PromptType:
    # Implement the logic to identify the prompt type based on the user message and context
    pass


async def process_prompt_request(prompt_request: PromptRequest, prompt_type: PromptType) -> None:
    # Implement the logic to process the prompt request based on the identified prompt type
    match(prompt_type):
        case PromptType.CREATE_COURSE:
            # Handle create course logic
            pass
        case PromptType.CREATE_MODULE:
            # Handle create module logic
            pass
        case PromptType.CREATE_LESSON:
            # Handle create lesson logic
            pass
        case PromptType.VOCABULARY:
            # Handle vocabulary logic
            pass
        case PromptType.EXERCISE:
            # Handle exercise logic
            pass
        case _:
            # Handle unknown prompt type
            pass



async def offer_options(prompt_request: PromptRequest) -> list[PromptOption]:
    # Implement the logic to offer options to the user based on the prompt request
    pass


async def handle_prompt_request(prompt_request: PromptRequest) -> None:
    prompt_type = await identify_prompt_type(prompt_request)
    # Implement the logic to handle the prompt request based on the identified prompt type
    prompt_type = await identify_prompt_type(prompt_request)
    if not prompt_type:








