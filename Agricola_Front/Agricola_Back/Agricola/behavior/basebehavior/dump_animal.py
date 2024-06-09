"""
동물 버리기 기초 행동
:param: 플레이어 번호, 버리고자 하는 동물의 종류와 위치
:return: 동물 버리기 성공 여부
:rtype: bool
"""
from behavior.basebehavior.base_behavior_interface import BaseBehaviorInterface
from command import Command
from entity.animal_type import AnimalType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


class DumpAnimal(BaseBehaviorInterface):
    def __init__(self, kind, pos):
        self.kind = kind
        self.pos = pos
        self.log_text = ""

    def execute(self):
        if player_status_repository.player_status[game_status_repository.game_status.now_turn_player].farm.field[self.pos[0]][self.pos[1]].count <= 0:
            self.log_text = "동물이 없습니다."
            return False
        else:
            player_status_repository.player_status[game_status_repository.game_status.now_turn_player].farm.field[ \
                self.pos[0]][self.pos[1]] -= 1
            if player_status_repository.player_status[game_status_repository.game_status.now_turn_player].farm.field[self.pos[0]][self.pos[1]].count == 0:
                player_status_repository.player_status[game_status_repository.game_status.now_turn_player].farm.field[ self.pos[0]][self.pos[1]].kind = AnimalType.NONE
            self.log_text = "동물 버리기 완료."

    def log(self):
        pass