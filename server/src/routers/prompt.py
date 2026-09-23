from fastapi import APIRouter, Depends, HTTPException
from models.prompts_old import PromptRequest, PromptResponse, PromptResponseType, PromptRouterType, PromptActionType, PromptResultsType

router = APIRouter()

@router.post("/prompt", response_model=PromptResponse)
async def handle_prompt(request: PromptRequest):
    # Implement the logic to handle the prompt request here
    # For now, just raise an HTTPException to indicate it's not implemented
    raise HTTPException(status_code=501, detail="Not implemented")
