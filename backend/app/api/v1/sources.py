from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.source import Source
from app.models.source import Source as SourceModel

router = APIRouter()

@router.get("/sources", response_model=list[Source])
async def list_sources(db: Session = Depends(get_db)):
    return db.query(SourceModel).limit(1000).all()

