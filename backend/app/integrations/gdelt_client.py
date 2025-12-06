import httpx
from app.core.config import settings

class GDELTClient:
    BASE_URL = "https://api.gdeltproject.org/api/v2/doc/doc"

    def __init__(self):
        self.api_key = settings.GDELT_API_KEY

    def search(self, query: str):
        params = {"query": query, "mode": "ArtList", "format": "json"}
        if self.api_key:
            params["apiKey"] = self.api_key
        response = httpx.get(self.BASE_URL, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        articles = data.get("articles", []) if isinstance(data, dict) else []
        return [
            {
                "title": a.get("title"),
                "url": a.get("url"),
                "domain": a.get("domain"),
                "snippet": a.get("excerpt"),
                "score": float(a.get("seccount", 0)),
            }
            for a in articles
        ]

