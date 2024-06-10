"""
:param: 바꾸고자 하는 동물 배치 상태
:return: 동물 배치 결과 리턴
:rtype: bool
동물 획득 과정
    1. 동물 획득 시 동물 큐로 받기
    2. 그 즉시 프론트에서 해당 동물 큐로 동물 배치 시작하기
    3. 동물 -> 배치하기

    이 커맨드는 동물을 배치하는 커맨드
"""
from copy import deepcopy

from behavior.validation.animal_position_validation import AnimalPositionValidation
from command import Command
# from repository.game_status_repository import game_status_repository
# from repository.player_status_repository import player_status_repository


class PlaceAnimal(Command):
    def __init__(self, field_status):
        self.log_text = ""
        self.field_status = deepcopy(field_status)

    def execute(self):
        if AnimalPositionValidation(self.field_status).execute():
            self.log_text = "동물 배치에 성공했습니다."
            player_status_repository.player_status[
                game_status_repository.game_status.now_turn_player].farm.field = self.field_status
            return True
        self.log_text = "올바르지 않은 동물 배치 : 동물을 올바르게 배치해주세요."
        return False

    def log(self):
        return self.log_text
