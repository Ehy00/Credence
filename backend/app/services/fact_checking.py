from typing import List
from app.integrations.openai_client import OpenAIClient

async def generate_verdict(claim: str, evidence: List[dict], client: OpenAIClient) -> dict:
    prompt = (
        "You are a fact-checking assistant. Given a claim and evidence snippets, "
        "return a JSON object with label (True/False/Misleading/Unverified), confidence (0-1), and rationale."
    )
    return await client.fact_check(claim, evidence, prompt)

