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


@dataclass
class RotateGridBlock(MapBlock):
    map_x: int
    map_y: int


class RotationType(Enum):
    CLOCKWISE = 1
    FLIP = 2
    COUNTERCLOCKWISE = 3


class PieceName(Enum):
    LONG_I = 1
    ORANGE_L = 2
    BLUE_L = 3
    LIME_Z = 4
    RED_Z = 5
    PINK_T = 6
    SQUARE = 7