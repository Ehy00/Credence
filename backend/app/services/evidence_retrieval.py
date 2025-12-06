from typing import List
from app.integrations.gdelt_client import GDELTClient
from app.integrations.google_factcheck_client import GoogleFactCheckClient
from app.integrations.mbfc_client import MBFCClient

def rank_evidence(results: List[dict], mbfc: MBFCClient) -> List[dict]:
    ranked = []
    for item in results:
        credibility = mbfc.get_score(item.get("domain"))
        ranked.append({**item, "credibility": credibility, "relevance": item.get("score", 0)})
    return sorted(ranked, key=lambda x: (x.get("relevance", 0) + (x.get("credibility") or 0)), reverse=True)

def retrieve_evidence(query: str, gdelt: GDELTClient, google_factcheck: GoogleFactCheckClient, mbfc: MBFCClient) -> List[dict]:
    # Get results from both GDELT and Google Fact Check
    gdelt_results = gdelt.search(query)
    google_results = google_factcheck.search(query)
    
    # Combine results
    all_results = gdelt_results + google_results
    
    # Rank and return top results
    return rank_evidence(all_results, mbfc)[:20]  # Return top 20

