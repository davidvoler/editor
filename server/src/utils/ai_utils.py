# from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.openai import OpenAIProvider
import os

ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
openai_base_url = f"{ollama_base_url.rstrip('/')}/v1"


def get_ai_model(provider: str, model_name: str) -> OpenAIProvider:
    # if provider == "openai":
    #     return OpenAIModel(model_name=model_name, base_url=openai_base_url)
    if provider == "ollama":
        return OpenAIProvider(model_name=model_name, base_url=ollama_base_url)
    else:
        raise ValueError(f"Unsupported provider: {provider}")