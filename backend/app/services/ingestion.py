from typing import Optional
import httpx
from bs4 import BeautifulSoup

async def fetch_url(url: str) -> Optional[str]:
    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.text

def html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    return soup.get_text(separator=" ", strip=True)

def normalize_text(text: str) -> str:
    return " ".join(text.split())

