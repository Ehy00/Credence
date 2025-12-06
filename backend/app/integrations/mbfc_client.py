import pandas as pd
from app.core.config import settings

class MBFCClient:
    def __init__(self):
        try:
            self.df = pd.read_csv(settings.MBFC_DATA_PATH)
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["domain", "credibility"])

    def get_score(self, domain: str | None) -> float | None:
        if not domain:
            return None
        row = self.df[self.df["domain"] == domain]
        if row.empty:
            return None
        return float(row.iloc[0].get("credibility", 0.5))

