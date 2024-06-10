"""
기본 가족 늘리기 후 보조 설비 1개 라운드 행동
:param: 플레이어 번호, 선택한 보조 설비
:return: 실행 결과.
:rtype: bool
"""
from behavior.basebehavior.buy_sub_card import BuySubCard
from behavior.behavior_interface import BehaviorInterface
from behavior.unitbehavior.playable_sub_facility_listup import PlayableSubCardListup
from behavior.unitbehavior.use_worker import UseWorker
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository



class FamilyFacility(BehaviorInterface):

    def __init__(self,game_status,player_status,round_status):
        self.log_text = ""
        player = game_status_repository.game_status.now_turn_player
        self.player_status = player_status_repository.player_status[player]

    def can_play(self):
        if self.player_status.worker <= self.player_status.farm.get_house_count():
            self.log_text = "집이 부족합니다."
            return False
        if self.player_status.baby + self.player_status.worker == 5:
            self.log_text = "더 이상 가족을 늘릴 수 없습니다"
            return False
        return True

    def execute(self):
        self.player_status.set_baby(self.player_status.baby + 1)
        self.log_text = "급하지않은 가족 늘리기를 성공했습니다"
        return [PlayableSubCardListup, BuySubCard, UseWorker]

    def log(self):
        return self.log_text
