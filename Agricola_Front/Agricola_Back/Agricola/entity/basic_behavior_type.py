"""
기본 행동 Enum
"""

from enum import Enum


class BasicBehaviorType(Enum):
    WOOD1 = 0
    WOOD2 = 1
    MARKET = 2
    DIRT1 = 3
    THEATER = 4
    EXPAND = 5
    MEETING = 6
    SEED = 7
    CULTIVATE = 8
    SIDE_JOB1 = 9
    DAY_LABOR = 10
    WOOD3 = 11
    DIRT2 = 12
    REED = 13
    FISHING = 14
    SIDE_JOB2 = 15


basic_behavior_reverse_map = {member.value: member.name for member in BasicBehaviorType}