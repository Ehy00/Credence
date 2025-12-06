from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.core.security import get_api_key
from app.services.admin_service import override_verdict
from app.schemas.verdict import Verdict

router = APIRouter()

@router.post("/admin/verdicts/{verdict_id}", response_model=Verdict)
async def update_verdict(verdict_id: int, payload: dict, db: Session = Depends(get_db), api_key: str | None = Depends(get_api_key)):
    label = payload.get("label")
    confidence = payload.get("confidence")
    if not label:
        raise HTTPException(status_code=400, detail="label is required")
    verdict = override_verdict(db, verdict_id, label, confidence or 0.0)
    if not verdict:
        raise HTTPException(status_code=404, detail="Verdict not found")
    return verdict

