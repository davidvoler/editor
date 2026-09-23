from fastapi import APIRouter, Depends, HTTPException
from models.prompts_old import PromptContext
from models.context import ContextRequest
router = APIRouter()

@router.post("/context", response_model=PromptContext)
async def handle_context(request: ContextRequest):
    # Implement the logic to handle the context request here
    # For now, just raise an HTTPException to indicate it's not implemented
    raise HTTPException(status_code=501, detail="Not implemented")