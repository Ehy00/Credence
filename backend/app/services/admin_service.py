from sqlalchemy.orm import Session
from app.models.verdict import Verdict

def override_verdict(db: Session, verdict_id: int, label: str, confidence: float) -> Verdict:
    verdict = db.get(Verdict, verdict_id)
    if verdict:
        verdict.label = label
        verdict.confidence = confidence
        db.add(verdict)
        db.commit()
        db.refresh(verdict)
    return verdict

