# --- Vocab Schema ---
class VocabularyItem(BaseModel):
    word: str
    translation: str
    part_of_speech: str
    example_sentence: str
    sentence_translation: str

class VocabularyList(BaseModel):
    items: list[VocabularyItem]

# --- Exercise Schema (Your Existing Model) ---
class SingleChoice(BaseModel):
    sentence: str = Field(description="Target sentence with a blank or question context.")
    correct_answer: str = Field(description="The correct target word.")
    incorrect_options: list[str] = Field(description="3 plausible distractors.")
    translation: str = Field(description="Native translation.")

class SingleChoiceList(BaseModel):
    questions: list[SingleChoice]


# --- Sub-Agent Definitions ---
vocab_agent = Agent(
    'openai:gpt-4o',
    output_type=VocabularyList,
    system_prompt="You are a linguistic expert creating structured vocabulary lists for language courses."
)

quiz_agent = Agent(
    'openai:gpt-4o',
    output_type=SingleChoiceList,
    system_prompt="You are an expert assessment generator creating accurate single-choice language exercises."
)