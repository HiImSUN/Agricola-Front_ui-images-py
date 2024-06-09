from enum import Enum


class HouseType(Enum):
    NONE = 0
    DIRT = 1
    WOOD = 2
    STONE = 3


house_type_reverse_map = {member.value: member.name for member in HouseType}
