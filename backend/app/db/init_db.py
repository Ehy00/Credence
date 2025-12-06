import pandas as pd
from sqlalchemy.orm import Session
from app.db.session import engine, SessionLocal
from app.db import base
from app.models import source
from app.core.config import settings

def init_db() -> None:
    base.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_mbfc(db)
    finally:
        db.close()

def seed_mbfc(db: Session):
    if settings.MBFC_DATA_PATH and db.query(source.Source).count() == 0:
        try:
            df = pd.read_csv(settings.MBFC_DATA_PATH)
            for _, row in df.iterrows():
                db.add(
                    source.Source(
                        domain=row.get("domain"),
                        name=row.get("name"),
                        bias=row.get("bias"),
                        credibility=row.get("credibility"),
                        url=row.get("url"),
                    )
                )
            db.commit()
        except FileNotFoundError:
            print("MBFC dataset not found; skipping seed")

if __name__ == "__main__":
    init_db()

