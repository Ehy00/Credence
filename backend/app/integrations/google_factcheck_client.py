import httpx
from typing import List, Optional
from app.core.config import settings

class GoogleFactCheckClient:
    BASE_URL = "https://factchecktools.googleapis.com/v1alpha1/claims:search"

    def __init__(self):
        self.api_key = settings.GOOGLE_FACTCHECK_API_KEY

    def search(self, query: str, language_code: str = "en") -> List[dict]:
        """Search Google Fact Check API for fact-checked claims"""
        if not self.api_key:
            return []
        
        params = {
            "query": query,
            "languageCode": language_code,
            "key": self.api_key,
        }
        
        try:
            response = httpx.get(self.BASE_URL, params=params, timeout=15)
            response.raise_for_status()
            data = response.json()
            
            claims = data.get("claims", []) if isinstance(data, dict) else []
            results = []
            
            for claim in claims:
                # Extract claim text
                claim_text = claim.get("text", "")
                
                # Get review information
                review = claim.get("claimReview", [{}])[0] if claim.get("claimReview") else {}
                publisher = review.get("publisher", {})
                
                results.append({
                    "title": claim_text,
                    "url": review.get("url", ""),
                    "domain": publisher.get("site", ""),
                    "snippet": claim_text[:200],
                    "score": 1.0,  # Google Fact Check results are pre-verified
                    "rating": review.get("textualRating", ""),
                    "review_date": review.get("reviewDate", ""),
                })
            
            return results
        except Exception as e:
            print(f"Google Fact Check API error: {e}")
            return []

