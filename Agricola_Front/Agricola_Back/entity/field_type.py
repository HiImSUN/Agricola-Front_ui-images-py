"""
필드 타입을 지정하는 Enum 클래스
"""
from enum import Enum


class FieldType(Enum):
    NONE_FIELD = 0
    ARABLE = 1
    CAGE = 2
    HOUSE = 3
    FENCE = 4
