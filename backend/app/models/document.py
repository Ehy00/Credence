from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=True)
    title = Column(String, nullable=True)
    source_domain = Column(String, index=True, nullable=True)
    raw_text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    claims = relationship("Claim", back_populates="document", cascade="all, delete-orphan")

