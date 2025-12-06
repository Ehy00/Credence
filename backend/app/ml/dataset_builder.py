from sqlalchemy.orm import Session
from app.models.claim import Claim
from app.models.verdict import Verdict

def build_dataset(db: Session):
    rows = (
        db.query(Claim.text, Verdict.label, Verdict.confidence)
        .join(Verdict, Verdict.claim_id == Claim.id)
        .all()
    )
    return rows

