from pydantic import BaseModel, Field



class Language(BaseModel):
    code: str = Field(..., description="The ISO 639-1 code of the language")
    name_language_code: str = Field(..., description="The name in the language specified by the code")
    name: str = Field(..., description="The name of the language in the language specified by name_language_code")
    native_name: str = Field(..., description="The native name of the language")
    weight: int = Field(..., description="The weight of the language for ordering purposes")


