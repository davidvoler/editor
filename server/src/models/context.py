from pydantic import BaseModel

class ContextRequest(BaseModel):
    course_id: int|None = 0
    module_id: int|None = 0