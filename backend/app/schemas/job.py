from pydantic import BaseModel
from typing import Optional, List
from app.schemas.document import Document
from app.schemas.claim import Claim
from app.schemas.verdict import Verdict
from app.schemas.evidence import Evidence

class VerificationJob(BaseModel):
    job_id: str
    status: str
    document: Optional[Document] = None
    claims: List[Claim] = []
    verdicts: List[Verdict] = []
    evidences: List[Evidence] = []
    article_verdict: Optional[str] = None
    article_confidence: Optional[float] = None

    class Config:
        from_attributes = True

