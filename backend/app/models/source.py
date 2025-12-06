from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True, index=True)
    domain = Column(String, unique=True, index=True)
    name = Column(String, nullable=True)
    bias = Column(String, nullable=True)
    credibility = Column(Float, nullable=True)
    url = Column(String, nullable=True)

