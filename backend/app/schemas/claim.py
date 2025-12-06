from pydantic import BaseModel
from typing import Optional, List
from app.schemas.evidence import Evidence
from app.schemas.verdict import Verdict

class ClaimBase(BaseModel):
    text: str
    topic: Optional[str] = None
    confidence: Optional[float] = None

class ClaimCreate(ClaimBase):
    document_id: int

class Claim(ClaimBase):
    id: int
    evidences: List[Evidence] = []
    verdicts: List[Verdict] = []

    class Config:
        from_attributes = True

