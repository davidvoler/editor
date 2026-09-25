from fastapi import APIRouter, Depends, HTTPException
from models.prompts import PromptRequest
from models.tasks import TasksResultsRequest
from tasks.prompt_tasks import handle_prompt_task
router = APIRouter()

@router.post("/prompt", response_model=TasksResultsRequest)
async def _handle_prompt_(request: PromptRequest)->TasksResultsRequest:
   return await handle_prompt_task(request)
