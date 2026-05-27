import json
import logging
from pydantic import BaseModel, ValidationError

# Set up terminal logging to match the "Hype vs. Logs" article aesthetic
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# ---------------------------------------------------------
# 1. THE DEFENSIVE GATE: Define the exact schema we demand
# ---------------------------------------------------------
class AgentResponse(BaseModel):
    action: str
    tool_name: str
    parameters: dict
    confidence_score: float

# ---------------------------------------------------------
# 2. MOCK LLM CALL: Simulating the messy reality of production
# ---------------------------------------------------------
def mock_llm_call(prompt: str, force_error: bool = False) -> str:
    """Simulates an LLM returning a string. Sometimes it hallucinates markdown formatting."""
    if force_error:
        # The classic LLM mistake: wrapping JSON in markdown tags with wrong data types
        return "
http://googleusercontent.com/immersive_entry_chip/0

Once that pushes successfully, you have the article draft ready, the custom header image, and the actual backend code live on your profile to back it all up.

