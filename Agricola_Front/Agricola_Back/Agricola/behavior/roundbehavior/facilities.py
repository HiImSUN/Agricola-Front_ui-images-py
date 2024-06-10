"""
주요 설비/보조 설비 1개 놓기 라운드 행동
:param: 플레이어 번호, 선택한 카드
:return: 실행 결과.
:rtype: bool
"""
from behavior.basebehavior.buy_main_card import BuyMainCard
from behavior.basebehavior.buy_sub_card import BuySubCard
from behavior.behavior_interface import BehaviorInterface
from behavior.unitbehavior.playable_sub_facility_listup import PlayableSubCardListup
from behavior.unitbehavior.purchasable_main_facility_listup import PurchasableMainCardListup
from behavior.unitbehavior.use_worker import UseWorker


class Facilities(BehaviorInterface):
    def __init__(self,game_status,player_status,round_status):
        self.log_text = ""

    def can_play(self):
        return True

    def execute(self):
        ret = [PurchasableMainCardListup,BuyMainCard, PlayableSubCardListup, BuySubCard, UseWorker]
        return ret

    def log(self):
        return self.log_text
