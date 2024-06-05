"""
라운드 행동 Enum
"""
from enum import Enum


class RoundBehaviorType(Enum):
    SHEEP1 = 0
    FENCE = 1
    FACILITIES = 2
    SEED_BAKE = 3
    FAMILY_FACILITY = 4
    STONE_2 = 5
    UPGRADE_FACILITIES = 6
    PIG = 7
    VEGETABLE = 8
    COW = 9
    STONE_4 = 10
    CULTIVATE_SEED = 11
    HURRY_FAMILY = 12
    UPGRADE_FENCE = 13
