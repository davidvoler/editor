from pydantic import BaseModel, Field
from pydantic_ai import Agent
from prompts.providers import get_provider
from models.word import (WordTranslationList, WordTranslation)
from utils.ai_utils import get_ai_model


async def prompt_suggested_words(
   lang: str,
   to_lang: str,
   level: str,
   num_words: int = 30,
    provider: str = "ollama",
    model: str = "llama3.1") -> WordTranslationList:
    """Generate a list of words and their translations. for students speaking {to_lang} learning {lang}. """
    # model_instance = get_ai_model(provider, model)
    agent = Agent(
        f"{provider}:{model}",
        output_type=WordTranslationList,
        system_prompt=f"You are an expert {lang} language teacher.")
    
    result = await agent.run(f"Create {num_words} words in {lang} suitable for {level} learners and provide their translations in {to_lang}.")
    return result.output