from entity.farm.field import Field
from entity.field_type import FieldType

'''
집 구상 클래스
'''


class House(Field):
    def __init__(self):
        self.field_type = FieldType.HOUSE
