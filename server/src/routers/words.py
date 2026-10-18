from fastapi import APIRouter
from models.word import Word
from utils.words_utils import course_words

router = APIRouter()

@router.get("/words", response_model=list[Word])
async def _get_words(course_id: int, module_id: int | None = None) -> list[Word]:
    """The course's words, or the module's when module_id is given."""
    return await course_words(course_id, module_id)
