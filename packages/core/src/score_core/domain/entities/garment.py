from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Garment:
    kind: str                # e.g., "top", "bottom", "shoes", "outerwear"
    color_primary: str       # e.g., "black"
    color_secondary: Optional[str] = None
    material: Optional[str] = None
