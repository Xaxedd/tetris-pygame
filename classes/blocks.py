from dataclasses import dataclass
from typing import List


@dataclass
class MapBlock:
    x: int
    y: int
    color: List[int]
