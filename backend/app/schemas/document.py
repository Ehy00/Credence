from pydantic import BaseModel
from typing import List, Optional
from app.schemas.claim import Claim

class DocumentBase(BaseModel):
    url: Optional[str] = None
    title: Optional[str] = None
    source_domain: Optional[str] = None
    raw_text: str

class DocumentCreate(DocumentBase):
    pass

class Document(DocumentBase):
    id: int
    claims: List[Claim] = []

    class Config:
        from_attributes = True

