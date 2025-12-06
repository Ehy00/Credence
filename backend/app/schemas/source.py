from pydantic import BaseModel
from typing import Optional

class SourceBase(BaseModel):
    domain: str
    name: Optional[str] = None
    bias: Optional[str] = None
    credibility: Optional[float] = None
    url: Optional[str] = None

class SourceCreate(SourceBase):
    pass

class Source(SourceBase):
    id: int

    class Config:
        from_attributes = True

