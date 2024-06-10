"""
효율 교습
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
"""
from behavior.basebehavior.buy_job_card_1 import BuyJobCard1
from behavior.behavior_interface import BehaviorInterface
from behavior.unitbehavior.playable_sub_job_listup import PlayableJobCardListup
from behavior.unitbehavior.use_worker import UseWorker
from command import Command
from entity.basic_behavior_type import BasicBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository


class SideJob1(BehaviorInterface):

    def __init__(self):
        self.log_text = ""
        player = game_status_repository.game_status.now_turn_player
        self.player = player
        self.player_resource = player_status_repository.player_status[player].resource
        self.player_ownCard = player_status_repository.player_status[player].own_card
        self.is_filled = round_status_repository.round_status.put_basic[BasicBehaviorType.SIDE_JOB1.value]

    def can_play(self):
        if self.player_ownCard.hand_job_card and ((not self.player_ownCard.put_job_card) or self.player_resource.food >= 1):
            self.log_text = "직업을 낼 수 있습니다."
            return True
        else:
            self.log_text = "비용이 없어 행동이 불가능합니다"
            return False

    def execute(self):
        return [PlayableJobCardListup, BuyJobCard1, UseWorker]

    def log(self):
        return self.log_text
