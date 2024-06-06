"""
유랑 극단 기본 행동
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
"""
from command import Command
from entity.basic_behavior_type import BasicBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository


# Todo

class Theater(Command):
    def __init__(self, player):
        self.log_text = None
        self.game_status = game_status_repository.game_status
        self.player_resource = player_status_repository.player_status[player].resource
        self.is_filled = round_status_repository.round_status.put_basic[BasicBehaviorType.THEATER.value]

    def can_play(self):
        return True

    def execute(self):
        self.player_resource.set_food(
            self.player_resource.food + self.game_status.basic_resource[BasicBehaviorType.THEATER.value])
        self.log_text = f"음식 {self.game_status.basic_resource[BasicBehaviorType.THEATER.value]}개를 획득하였습니다."
        self.game_status.set_basic_resource(BasicBehaviorType.THEATER.value, 0)
        return True

    def log(self):
        return self.log_text
