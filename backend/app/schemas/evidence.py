from pydantic import BaseModel
from typing import Optional

class EvidenceBase(BaseModel):
    claim_id: int
    source_domain: Optional[str] = None
    url: Optional[str] = None
    snippet: Optional[str] = None
    credibility: Optional[float] = None
    relevance: Optional[float] = None

class EvidenceCreate(EvidenceBase):
    pass

class Evidence(EvidenceBase):
    id: int

    class Config:
        from_attributes = True

