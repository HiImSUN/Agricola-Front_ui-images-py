"""
농장의 상태
"""
from typing import List

from entity.animal_type import AnimalType
from entity.farm.cage import Cage
from entity.farm.field import Field
from entity.farm.house import House
from entity.farm.none_field import NoneField
from entity.field_type import FieldType
from entity.house_type import HouseType


class Farm:
    def __init__(self):
        self.observers = []
        self.house_status = HouseType.WOOD
        self.field: List[List[Field]] = [[NoneField() for i in range(5)] for j in range(3)]
        self.field[2][0] = House()
        self.field[1][0] = House()
        self.horizon_fence = [[False for i in range(5)] for j in range(4)]
        self.vertical_fence = [[False for i in range(6)] for j in range(3)]
        self.pet = AnimalType.COW

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def set_house_status(self, house_status):
        self.house_status = house_status
        self.notify()

    def set_field(self, row, col, field):
        self.field[row][col] = field
        self.notify()

    def set_horizon_fence(self, row, col, horizon_fence):
        self.horizon_fence[row][col] = horizon_fence
        self.notify()

    def set_vertical_fence(self, row, col, vertical_fence):
        self.vertical_fence[row][col] = vertical_fence
        self.notify()

    def set_pet(self, pet):
        self.pet = pet
        self.notify()

    def get_cow_count(self):
        ret = 0
        if self.pet == "COW":
            ret += 1
        for fields in self.field:
            for field in fields:
                if field.kind == "COW":
                    print(field.count,end="")
                    ret += field.count
        return ret

    def get_pig_count(self):
        ret = 0
        if self.pet == "PIG":
            ret += 1
        for fields in self.field:
            for field in fields:
                if field.kind == "PIG":
                    ret += field.count
        return ret

    def get_sheep_count(self):
        ret = 0
        if self.pet == "SHEEP":
            ret += 1
        for fields in self.field:
            for field in fields:
                if field.kind == "SHEEP":
                    ret += field.count
        return ret

    def get_fence_count(self):
        ret = 0
        for fields in self.horizon_fence:
            for fence in fields:
                if fence is True:
                    ret += 1
        for fields in self.vertical_fence:
            for fence in fields:
                if fence is True:
                    ret += 1
        return ret

    def get_barn_count(self):
        ret = 0
        for fields in self.field:
            for field in fields:
                if field.barn is True:
                    ret += 1
        return ret

    def get_house_count(self):
        ret = 0
        for fields in self.field:
            for field in fields:
                if field.field_type == FieldType.HOUSE:
                    ret += 1
        return ret

    def get_arable_count(self):
        ret = 0
        for fields in self.field:
            for field in fields:
                if field.field_type == FieldType.ARABLE:
                    ret += 1
        return ret

    def get_none_field_count(self):
        ret = 0
        for fields in self.field:
            for field in fields:
                if isinstance(field,NoneField):
                    ret += 1
        return ret

    def get_cage_count(self):
        ret = 0
        for fields in self.field:
            for field in fields:
                if isinstance(field, Cage):
                    ret += 1
        return ret
