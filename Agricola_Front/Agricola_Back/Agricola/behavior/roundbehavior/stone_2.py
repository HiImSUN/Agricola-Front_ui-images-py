"""
채석장 라운드 행동 - 2주기
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
"""
from behavior.behavior_interface import BehaviorInterface
from behavior.unitbehavior.use_worker import UseWorker
from command import Command
from entity.round_behavior_type import RoundBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository


class Stone2(BehaviorInterface):
    def __init__(self,game_status,player_status,round_status, player):
        self.log_text = ""
        self.game_status = game_status_repository.game_status
        self.player_resource = player_status_repository.player_status[player].resource
        self.is_filled = round_status_repository.round_status.put_basic[stone2_card_index]

    def can_play(self):
        return True

    def execute(self):
        stone2_card_index = game_status_repository.game_status.get_stone2_card_index()
        self.player_resource.set_stone(
            self.player_resource.stone + self.game_status.round_resource[stone2_card_index])
        self.log_text = f"돌 {self.game_status.round_resource[stone2_card_index]}개를 획득하였습니다."
        self.game_status.set_round_resource(stone2_card_index, 0)
        return [UseWorker]

    def log(self):
        return self.log_text
