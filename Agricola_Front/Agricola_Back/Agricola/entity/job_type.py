"""
직업 타입 Enum
"""

from enum import Enum


class JobType(Enum):
    GREENGROCER = 0
    HEDGER = 1
    KILN_BAKER = 2
    LIVESTOCK_DEALER = 3
    LUMBERJACK = 4
    MAGICIAN = 5
    PRIEST = 6
    ROOFER = 7
    SKILLED_BRICKLAYER = 8
    SMALL_FARMER = 9
    SUB_CULTIVATOR = 10
    WAREHOUSE_MANAGER = 11


job_type_reverse_map = {member.value: member.name for member in JobType}