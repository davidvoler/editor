from urllib import request

from fastapi import APIRouter, Depends, HTTPException
from models.prompts import PromptRequest, PromptResponse
from models.tasks import TasksResultsRequest
from tasks.prompt_tasks import handle_prompt_task
from utils.prompt_utils import get_last_responses
router = APIRouter()

@router.post("/prompt", response_model=TasksResultsRequest)
async def _handle_prompt_(request: PromptRequest)->TasksResultsRequest:
   return await handle_prompt_task(request)


@router.get("/history", response_model=list[PromptResponse])
async def _handle_prompt_history_(course_id:int, module_id:int = 0, limit:int = 20)->list[PromptResponse]:
    return await get_last_responses(course_id, module_id, limit)
