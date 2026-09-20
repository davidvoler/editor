from typing import Literal, Union, Optional
from pydantic import BaseModel, Field

# --- Action Parameter Payload Types ---

class CreateCourseParams(BaseModel):
    action: Literal["create_course"] = "create_course"
    title: str = Field(description="Title of the course or overall topic")
    target_language: str = Field(description="Language being taught, e.g. 'Spanish'")
    native_language: str = Field(description="Language of instruction, e.g. 'English'")

class GenerateVocabParams(BaseModel):
    action: Literal["generate_vocab"] = "generate_vocab"
    topic: str = Field(description="Theme or topic, e.g., 'ordering food', 'airports'")
    num_words: int = Field(default=5, description="Number of words to generate")

class GenerateQuizParams(BaseModel):
    action: Literal["generate_quiz"] = "generate_quiz"
    word_list: list[str] = Field(default_factory=list, description="Specific target words to test, if mentioned")
    num_questions: int = Field(default=3, description="Number of quiz questions requested")

class NeedsClarification(BaseModel):
    action: Literal["clarify"] = "clarify"
    response_text: str = Field(description="Friendly response explaining what wasn't clear.")
    suggested_options: list[str] = Field(
        description="2-4 suggested options for the user to choose or click next"
    )

# Union of all supported routing options
RouterResult = Union[
    CreateCourseParams,
    GenerateVocabParams,
    GenerateQuizParams,
    NeedsClarification
]