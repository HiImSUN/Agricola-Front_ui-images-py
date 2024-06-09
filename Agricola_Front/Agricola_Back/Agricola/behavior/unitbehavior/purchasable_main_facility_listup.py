"""
구매 가능한 주요 설비 리스트업 함수
:param: void
:return: 구매 가능한 주요 설비 리스트 반환
:rtype: list<card_name>
"""
from behavior.main_facility.dirt_kiln import DirtKiln
from behavior.main_facility.oven1 import Oven1
from behavior.main_facility.oven2 import Oven2
from behavior.main_facility.strong_oven1 import StrongOven1
from behavior.main_facility.strong_oven2 import StrongOven2
from command import Command
from repository.game_status_repository import game_status_repository


class PurchasableMainCardListup(Command):
    def execute(self):
        card_list = []
        for index, card in enumerate(game_status_repository.game_status.main_facility_status):
            if card == -1:
                if index == 0:
                    card_list.append(Oven1)
                elif index == 1:
                    card_list.append(Oven2)
                elif index == 2:
                    card_list.append(StrongOven1)
                elif index == 3:
                    card_list.append(StrongOven2)
                elif index == 4:
                    card_list.append(DirtKiln)
        return card_list

    def log(self):
        pass