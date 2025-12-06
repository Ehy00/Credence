from typing import List

def aggregate_article_verdict(claim_verdicts: List[dict]) -> dict:
    if not claim_verdicts:
        return {"article_verdict": "Unverified", "article_confidence": 0.0}
    label_scores = {"True": 1.0, "False": -1.0, "Misleading": -0.5, "Unverified": 0.0}
    total = sum(label_scores.get(v.get("label"), 0) * v.get("confidence", 0) for v in claim_verdicts)
    avg_conf = sum(v.get("confidence", 0) for v in claim_verdicts) / len(claim_verdicts)
    label = "True" if total > 0.2 else "False" if total < -0.2 else "Misleading" if total < 0 else "Unverified"
    return {"article_verdict": label, "article_confidence": round(avg_conf, 2)}

