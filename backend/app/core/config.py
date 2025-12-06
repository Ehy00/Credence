from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings
from typing import List
from pydantic import AnyHttpUrl

# Get project root (two levels up from this file)
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./data/credence.db"
    OPENAI_API_KEY: str = ""
    GDELT_API_KEY: str = ""
    GOOGLE_FACTCHECK_API_KEY: str = ""
    MBFC_DATA_PATH: str = "./data/mbfc.csv"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]

    class Config:
        env_file = str(PROJECT_ROOT / ".env")
        case_sensitive = True

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()

