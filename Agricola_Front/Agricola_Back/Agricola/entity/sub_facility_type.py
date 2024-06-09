"""
보조 설비 Enum
"""

from enum import Enum


class SubFacilityType(Enum):
    BASKET = 0
    BOTTLE = 1
    CANOE = 2
    GIANT_FARM = 3
    GRAIN_SHOVEL = 4
    JUNK_WAREHOUSE = 5
    LOAM_MINING_SITE = 6
    MANGER = 7
    PINCER = 8
    PITCHFORK = 9
    SILPAN = 10
    WOOL = 11


sub_facility_type_reverse_map = {member.value: member.name for member in SubFacilityType}