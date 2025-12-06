from pydantic import BaseModel
from typing import Optional

class VerdictBase(BaseModel):
    claim_id: int
    label: str
    confidence: float
    rationale: Optional[str] = None
    model_version: Optional[str] = None

class VerdictCreate(VerdictBase):
    pass

class Verdict(VerdictBase):
    id: int

    class Config:
        from_attributes = True

