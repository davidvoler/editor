from pydantic import BaseModel, Field

class Word(BaseModel):
    text: str = Field(..., description="The word.")
    used: bool = Field(..., description="Indicates whether the word has been used.")
    

    
