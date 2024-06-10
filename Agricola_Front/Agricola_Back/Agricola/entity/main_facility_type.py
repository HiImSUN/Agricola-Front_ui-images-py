"""
주요 설비 Enum
"""

from enum import Enum


class MainFacilityType(Enum):
    DIRT_KILN = 0
    OVEN1 = 1
    OVEN2 = 2
    STRONG_OVEN1 = 3
    STRONG_OVEN2 = 4


main_facility_type_reverse_map = {member.value: member.name for member in MainFacilityType}