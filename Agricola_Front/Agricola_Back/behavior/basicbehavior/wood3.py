"""
나무 누적 3개 기본 행동 구현
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
Unit : 지민
"""
from command import Command
from entity.basic_behavior_type import BasicBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository


class Wood3(Command):
    def __init__(self, player):
        self.log_text = None
        self.game_status = game_status_repository.game_status
        self.player_resource = player_status_repository.player_status[player].resource
        self.is_filled = round_status_repository.round_status.put_basic[BasicBehaviorType.WOOD3.value]

    def execute(self):
        if self.is_filled:
            self.log_text = "이번 라운드에 이미 수행된 행동입니다."
            return False
        self.player_resource.set_wood(
            self.player_resource.wood + self.game_status.basic_resource[BasicBehaviorType.WOOD3.value])
        self.log_text = f"나무 {self.game_status.basic_resource[BasicBehaviorType.WOOD3.value]}개를 획득하였습니다."
        self.game_status.set_basic_resource(BasicBehaviorType.WOOD3.value, 0)
        return True

    def log(self):
        return self.log_text
