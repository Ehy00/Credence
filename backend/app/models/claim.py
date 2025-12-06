from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base import Base

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    text = Column(String, nullable=False)
    topic = Column(String, nullable=True)
    confidence = Column(Float, nullable=True)

    document = relationship("Document", back_populates="claims")
    evidences = relationship("Evidence", back_populates="claim", cascade="all, delete-orphan")
    verdicts = relationship("Verdict", back_populates="claim", cascade="all, delete-orphan")

