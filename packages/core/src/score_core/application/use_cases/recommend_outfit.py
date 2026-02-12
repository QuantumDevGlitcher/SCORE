from dataclasses import dataclass
from typing import List

from score_core.domain.entities.garment import Garment

@dataclass
class Recommendation:
    items: List[Garment]
    score: float
    explanation: str

def recommend_outfits(current: List[Garment], context: str) -> List[Recommendation]:
    # Placeholder: later replaced by fuzzy scoring + recommender + RL personalization
    return [
        Recommendation(items=current, score=50.0, explanation=f"Stub recommendation for context: {context}")
    ]
