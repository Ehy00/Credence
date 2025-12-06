from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)

async def get_api_key(api_key: str | None = Depends(API_KEY_HEADER)) -> str | None:
    # Placeholder for future auth; currently open
    if api_key is None:
        return None
    if api_key != "admin-key":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key"
        )
    return api_key

