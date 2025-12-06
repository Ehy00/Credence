from typing import List
from app.integrations.openai_client import OpenAIClient

async def extract_claims(text: str, client: OpenAIClient) -> List[dict]:
    prompt = (
        "Extract up to 5 fact-checkable claims from the article. "
        "Return JSON with fields: text, topic, confidence (0-1)."
    )
    return await client.extract_claims(text, prompt)

