from typing import List
import numpy as np

def embed_texts(texts: List[str]) -> List[List[float]]:
    # Placeholder deterministic embedding for demo
    return [list(np.random.rand(10)) for _ in texts]

