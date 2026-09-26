from pydantic import BaseModel
from models.exercise import Exercise
class Lesson(BaseModel):
    course_id: int|None = None
    module_id: int|None = None
    lesson_id: int|None = None
    title: str|None = None
    description: str|None = None
    words: list[str]|None = None
    sentences: list[str]|None = None
    deleted: bool|None = False
    weight: int|None = 0

class LessonFull(Lesson):
    lesson: Lesson|None = None
    exercises: list[Exercise]|None = None