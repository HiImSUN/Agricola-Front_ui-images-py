from copy import deepcopy
from typing import List

from behavior.validation.animal_move_validation import AnimalMoveValidation
from command import Command
from entity.farm.field import Field
from entity.farm.none_field import NoneField
from entity.field_type import FieldType


class MoveAnimal(Command):
    def __init__(self, field_status, animal_type, position):
        self.field_status = deepcopy(field_status)
        self.animal_type = animal_type
        self.position = position

    def execute(self):
        expanded_field: List[List[Field]] = [[NoneField() for _ in range(11)] for _ in range(11)]
        for i in range(3):
            for j in range(5):
                expanded_field[i * 2 + 1][j * 2 + 1] = self.field_status[i][j]
        for i in range(4):
            for j in range(5):
                expanded_field[i * 2][j * 2 + 1].field_type = FieldType.FENCE
        for i in range(3):
            for j in range(6):
                expanded_field[i * 2 + 1][j * 2].field_type = FieldType.FENCE
        return AnimalMoveValidation(expanded_field, self.animal_type, self.position).execute()

    def log(self):
        pass