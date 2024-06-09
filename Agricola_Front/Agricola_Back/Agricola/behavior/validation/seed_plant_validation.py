"""
:param: 변하고자 하는 필드 상태,
"""
from copy import deepcopy

from command import Command
from entity.crop_type import CropType
from entity.field_type import FieldType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


class SeedPlantValidation(Command):

    def __init__(self, plantDict):
        self.plantDict = plantDict
        self.field_status = deepcopy(player_status_repository.player_status[game_status_repository.game_status.now_turn_player].farm.field)
        self.log_text = ""

    def execute(self):
        vegetable_count = 0
        grain_count = 0
        if CropType.VEGETABLE in self.plantDict:
            for selectArable in self.plantDict[CropType.VEGETABLE]:
                vegetable_count += 1
                validationField = self.field_status[selectArable[0]][selectArable[1]]
                if validationField.fieldType != FieldType.ARABLE and validationField.kind != CropType.NONE:
                    self.log_text = "심을 수 없는 위치 입니다"
                    return False
        if CropType.GRAIN in self.plantDict:
            for selectArable in self.plantDict[CropType.GRAIN]:
                grain_count += 1
                validationField = self.field_status[selectArable[0]][selectArable[1]]
                if validationField.fieldType != FieldType.ARABLE and validationField.kind != CropType.NONE:
                    self.log_text = "심을 수 없는 위치 입니다"
                    return False
        if grain_count > player_status_repository.player_status[game_status_repository.game_status.now_turn_player].resource.grain:
            self.log_text = "곡식이 모자랍니다."
            return False
        if vegetable_count > player_status_repository.player_status[game_status_repository.game_status.now_turn_player].resource.vegetable:
            self.log_text = "채소가 모자랍니다."
            return False
        self.log_text = "밭 심기 검증 성공"
        return True

    def log(self):
        return self.log_text
