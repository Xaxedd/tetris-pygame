from dataclasses import dataclass
from enum import Enum
from typing import List


class Side(Enum):
    BOTTOM = 0
    LEFT = 1
    RIGHT = 2


@dataclass
class MapBlock:
    x: int
    y: int
    color: List[int]
