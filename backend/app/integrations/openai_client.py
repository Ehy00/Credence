import json
from typing import List
from openai import AsyncOpenAI
from app.core.config import settings

class OpenAIClient:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

    async def extract_claims(self, text: str, prompt: str) -> List[dict]:
        response = await self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": prompt}, {"role": "user", "content": text}],
            response_format={"type": "json_object"},
        )
        payload = response.choices[0].message.content
        data = json.loads(payload)
        return data.get("claims", []) if isinstance(data, dict) else []

    async def fact_check(self, claim: str, evidence: List[dict], prompt: str) -> dict:
        evidence_text = "\n".join([f"- {item.get('snippet', '')}" for item in evidence])
        response = await self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {
                    "role": "user",
                    "content": f"Claim: {claim}\nEvidence:\n{evidence_text}",
                },
            ],
            response_format={"type": "json_object"},
        )
        payload = response.choices[0].message.content
        try:
            return json.loads(payload)
        except json.JSONDecodeError:
            return {"label": "Unverified", "confidence": 0.0, "rationale": payload}

