from urllib import request

from fastapi import APIRouter, Depends, HTTPException
from models.prompts import PromptOption, PromptRequest, PromptResponse, PromptOption
from models.tasks import TasksResultsRequest
from tasks.prompt_tasks import handle_prompt_task
from utils.prompt_utils import get_last_responses
from prompt_routers.course import default_course_options
router = APIRouter()

@router.post("/prompt", response_model=TasksResultsRequest)
async def _handle_prompt(request: PromptRequest)->TasksResultsRequest:
   print(f"Handling prompt request: {request}")
   return await handle_prompt_task(request)


@router.get("/history", response_model=list[PromptResponse])
async def _handle_prompt_history(course_id:int, module_id:int = 0, limit:int = 20)->list[PromptResponse]:
    return await get_last_responses(course_id, module_id, limit)


@router.get("/default_options", response_model=list[PromptOption])
async def _default_options(course_id:int)->list[PromptOption]:
    return default_course_options(course_id)


