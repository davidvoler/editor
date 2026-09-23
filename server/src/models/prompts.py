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
    prompt_type: PromptRouterType = Field(..., description="The type of prompt this option is associated with.")
    


class PromptRequest(BaseModel):
    user_message: str = Field(..., description="The message input from the user.") 
    context: PromptContext|None = Field(..., description="The context for the prompt, including course, module, and words.")
    provider: str = Field(..., description="The AI provider associated with the prompt request.")
    model: str = Field(..., description="The model to use for the prompt request.")





class PromptResponse(BaseModel):
    response_type: PromptResponseType = Field(..., description="The type of response expected for the prompt. ")
    prompt_request: PromptRequest = Field(..., description="The original prompt request associated with this response.")
    option: list[PromptOption]|None = Field(..., description="The option associated with this response, if applicable.")
    task_id: str|None = Field(..., description="The ID of the task associated with this response, if applicable.")
    results: any|None = Field(..., description="The results associated with this response, if applicable.")
    results_type: str|None = Field(..., description="The type of the results associated with this response, if applicable.")
    ui_chat_response: any|None = Field(..., description="The UI chat response associated with this response, if applicable.")
    prompt_router_type: PromptRouterType|None = Field(..., description="The type of prompt router associated with this response, if applicable.")
    prompt_sub_route: str|None = Field(..., description="The sub-route of the prompt associated with this response, if applicable.")
    prompt_action_type: PromptActionType|None = Field(..., description="The type of action associated with this response, if applicable.")
    

class PromptResultsType(Enum):
    OPTION = "option" # show the options 
    NEW_COURSE = "new_course"
    NEW_MODULE = "new_module"
    TASK_ID = "task_id" # show spinner and reload current module when spinner completes
    


class PromptRouterType(Enum):
    COURSE = "create_course"
    MODULE = "create_module"
    LESSON = "create_lesson"
    VOCABULARY = "vocabulary"
    EXERCISE = "exercise"
    VIDEO = "video"

class PromptActionType(Enum):
    OPTIONS = "options"
    ASK_AI = "ask_ai"
    CACHE = "cache"
    SIMPLE_ACTION = "simple_action" # like create elements 
    ATTRIBUTES = "attributes"


class ExercisePromptType(Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    FILL_IN_THE_BLANK = "fill_in_the_blank"
    TRUE_FALSE = "true_false"
    SINGLE_CHOICE = "single_choice"
    EXPLANATION = "explanation"

class LessonPromptType(Enum):
    CREATE_LESSON = "create_lesson"

class CoursePromptType(Enum):
    CREATE_COURSE = "create_course"
    COURSE_ATTRIBUTES = "course_attribute"

class ModulePromptType(Enum):
    CREATE_MODULE = "create_module"
    MODULE_ATTRIBUTES = "module_attribute"
    SUGGEST_WORDS = "suggest_words"

class VideoPromptType(Enum):
    SECTIONS = "sections"
    PARTS = "parts"

class PromptResponseType(Enum):
    TASK = "task" # we have to run a task as the response could take 10 - 30 seconds 
    SYNC = "sync" # answer should be returned synchronously - less than a second
    ASYNC = "async" # answer will be returned asynchronously - 1 - 5 seconds