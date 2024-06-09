from enum import Enum


class CropType(Enum):
    NONE = 0
    GRAIN = 1
    VEGETABLE = 2


crop_type_reverse_map = {member.value: member.name for member in CropType}
