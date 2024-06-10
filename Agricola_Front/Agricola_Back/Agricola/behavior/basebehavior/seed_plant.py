"""
:param plantDict: 심은 곡식 및 채소 위치
    ex)
:param field_status: 바꾸고자 하는 필드 상태
"""
from copy import deepcopy

from command import Command
from entity.crop_type import CropType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from behavior.validation.seed_plant_validation import SeedPlantValidation


class SeedPlant(Command):

    def __init__(self, plantDict, field_status):
        self.plantDict = plantDict
        self.field_status = deepcopy(field_status)
        self.log_text = ""

    def execute(self):
        seed_plant_validation = SeedPlantValidation(self.plantDict)
        if seed_plant_validation.execute():
            self.log_text = "종자 심기 검증에 성공했습니다"
            vegetable_count = 0
            grain_count = 0
            if CropType.VEGETABLE in self.plantDict:
                for selectArable in self.plantDict[CropType.VEGETABLE]:
                    vegetable_count += 1
            if CropType.GRAIN in self.plantDict:
                for selectArable in self.plantDict[CropType.GRAIN]:
                    grain_count += 1
            player_status_repository.player_status[
                game_status_repository.game_status.now_turn_player].resource.grain -= grain_count
            player_status_repository.player_status[
                game_status_repository.game_status.now_turn_player].resource.vegetable -= vegetable_count
            player_status_repository.player_status[
                game_status_repository.game_status.now_turn_player].farm.field = self.field_status
            return True
        else:
            self.log_text = seed_plant_validation.log()
            return False

    def log(self):
        return self.log_text
