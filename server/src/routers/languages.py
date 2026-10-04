from fastapi import APIRouter
from models.language import Language
from utils.language_utils import DEFAULT_UI_LANGUAGE, get_languages

router = APIRouter()

@router.get("/languages", response_model=list[Language])
async def _get_languages(ui_language: str = DEFAULT_UI_LANGUAGE) -> list[Language]:
    return get_languages(ui_language)
