from pydantic import BaseModel, Field
from enum import Enum
from server.src.models.course import Course
from server.src.models.module import Module
from server.src.models.word import Word

class PromptResultsType(Enum):
    OPTION = "option" # show the options 
    NEW_COURSE = "new_course"
    NEW_MODULE = "new_module"
    TASK_ID = "task_id" # show spinner and reload current module when spinner completes
    

# indicating which router took care of the prompt request
class PromptRouterType(Enum):
    COURSE = "create_course"
    MODULE = "create_module"
    LESSON = "create_lesson"
    VOCABULARY = "vocabulary"
    EXERCISE = "exercise"
    VIDEO = "video"
    MAIN = "main"
    UNKNOWN = "unknown"

class PromptActionType(Enum):
    OPTIONS = "options"
    ASK_AI = "ask_ai"
    CACHE = "cache"
    SIMPLE_ACTION = "simple_action" # like create elements 
    ATTRIBUTES = "attributes"


class PromptType(Enum):
    EXERCISE_MULTIPLE_CHOICE = "multiple_choice"
    EXERCISE_FILL_IN_THE_BLANK = "fill_in_the_blank"
    EXERCISE_TRUE_FALSE = "true_false"
    EXERCISE_SINGLE_CHOICE = "single_choice"
    EXERCISE_EXPLANATION = "explanation"
    LESSON_CREATE = "create_lesson"
    COURSE_CREATE = "create_course"
    COURSE_ATTRIBUTE = "course_attribute"
    MODULE_CREATE = "create_module"
    MODULE_ATTRIBUTE = "module_attribute"
    MODULE_SUGGEST_WORDS = "suggest_words"
    VIDEO_SECTIONS = "video_sections"
    VIDEO_PARTS = "video_parts"


class PromptOptionData(BaseModel):
    label: str = Field(..., description="The label of the prompt option.")
    field_name: str = Field(..., description="The name of the field associated with the prompt option.")
    value: str|None = Field(..., description="The value associated with the prompt option.")
    

class PromptOption(BaseModel):
    option_text: str = Field(..., description="The text of the option.")
    option_value: str = Field(..., description="The value associated with the option.")
    prompt_type: PromptRouterType = Field(..., description="The type of prompt this option is associated with.")
    option_data: list[PromptOptionData]|None = Field(..., description="The data associated with the prompt option.")
    selected: bool = Field(..., description="Indicates whether this option is selected.")
    

class PromptRequest(BaseModel):
    course: Course|None = Field(..., description="The course context for the prompt.")
    module: Module|None = Field(..., description="The module context for the prompt.")
    words_list: list[Word]|None = Field(..., description="The list of words in the context.")
    course_id: int|None = Field(..., description="The ID of the course in the context.")
    module_id: int|None = Field(..., description="The ID of the module in the context.")
    lesson_id: int|None = Field(..., description="The ID of the lesson in the context.")
    user_message: str = Field(..., description="The message input from the user.") 
    provider: str = Field(..., description="The AI provider associated with the prompt request.")
    model: str = Field(..., description="The model to use for the prompt request.")
    options: list[PromptOption]|None = Field(..., description="The list of options associated with the prompt request.")
    last_router_type: PromptRouterType|None = Field(..., description="The type of prompt router associated with the prompt request.")
    last_action_type: PromptActionType|None = Field(..., description="The type of action associated with the last prompt request.")


class PromptResponse(BaseModel):
    prompt_request: PromptRequest = Field(..., description="The original prompt request associated with this response.")
    course: Course|None = Field(..., description="The course context for the response.")
    module: Module|None = Field(..., description="The module context for the response.")
    course_id: int|None = Field(..., description="The ID of the course in the context.")
    module_id: int|None = Field(..., description="The ID of the module in the context.")
    lesson_id: int|None = Field(..., description="The ID of the lesson in the context.")
    option: list[PromptOption]|None = Field(..., description="The option associated with this response, if applicable.")
    task_id: str|None = Field(..., description="The ID of the task associated with this response, if applicable.")
    results: any|None = Field(..., description="The results associated with this response, if applicable.")
    results_type: str|None = Field(..., description="The type of the results associated with this response, if applicable.")
    ui_chat_response: any|None = Field(..., description="The UI chat response associated with this response, if applicable.")
    prompt_router_type: PromptRouterType|None = Field(..., description="The type of prompt router associated with this response, if applicable.")
    prompt_type: PromptType|None = Field(..., description="The type of prompt associated with this response, if applicable.")
    prompt_action_type: PromptActionType|None = Field(..., description="The type of action associated with this response, if applicable.")
    

