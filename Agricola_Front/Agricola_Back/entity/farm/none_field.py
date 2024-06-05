"""
null값의 역할을 수행하는 noneField
"""
from entity.animal_type import AnimalType
from entity.farm.field import Field
from entity.field_type import FieldType


class NoneField(Field):
    def __init__(self):
        self.field_type = FieldType.CAGE
        self.kind = AnimalType.NONE
        self.count = 0
        self.maximum = 0
        self.barn = True
