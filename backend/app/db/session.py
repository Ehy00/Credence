from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import os

# Use connection pooling for serverless (Vercel)
if os.getenv("VERCEL"):
    # Serverless: use connection pooling to handle cold starts
    engine = create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        pool_size=1,
        max_overflow=0,
        connect_args={"connect_timeout": 10}
    )
else:
    # Local development: standard connection
    engine = create_engine(settings.DATABASE_URL, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

