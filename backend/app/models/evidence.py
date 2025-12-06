from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Evidence(Base):
    __tablename__ = "evidence"

    id = Column(Integer, primary_key=True, index=True)
    claim_id = Column(Integer, ForeignKey("claims.id"), nullable=False)
    source_domain = Column(String, nullable=True)
    url = Column(String, nullable=True)
    snippet = Column(Text, nullable=True)
    credibility = Column(Float, nullable=True)
    relevance = Column(Float, nullable=True)

    claim = relationship("Claim", back_populates="evidences")

