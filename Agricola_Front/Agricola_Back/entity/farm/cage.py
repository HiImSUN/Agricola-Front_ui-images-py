from entity.animal_type import AnimalType
from entity.farm.field import Field
from entity.field_type import FieldType

'''
울타리 정보
한 칸별로 생성
한칸당 최대 2마리까지 수용
외양간 존재 시 4마리까지 수용
'''


class Cage(Field):
    def __init__(self):
        self.field_type = FieldType.CAGE
        self.kind = AnimalType.NONE
        self.count = 0
        self.maximum = 0
        self.barn = False
