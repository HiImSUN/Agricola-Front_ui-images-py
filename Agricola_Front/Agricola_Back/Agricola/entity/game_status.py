"""
게임 전체의 진행 상태를 저장하는 클래스
"""

from entity.main_facility_status import MainFacilityStatus
from entity.round_behavior_type import RoundBehaviorType


class GameStatus:
    def __init__(self):
        self.observers = []
        self.now_round = 0  # 현재 라운드
        self.now_turn_player = 0  # 현재 턴 플레이어
        self.next_turn_player = 0  # 다음 턴 플레이어
        self.round_card_order = [0 for i in range(14)]  # 라운드 카드의 순서. reverse map으로 탐색
        self.round_card_put = [None for i in range(14)] 
        self.basic_card_put = [None for i in range(16)] 
        self.opened_round = [False for i in range(14)]  # 해당 라운드의 카드 공개 여부
        self.round_resource = [0 for i in range(14)]  # 라운드 기준 해당 라운드 칸 내부 자원 수 -> 프론트가 자원 표기하기 좋도록
        self.basic_resource = [0 for i in range(16)]  # 행동 Enum 기준 해당 행동 칸 내부 자원 수
        self.worker_count = [2,2,2,2]
        self.main_facility_status = MainFacilityStatus()
        self.acted = False
    def round_reset(self):
        self.worker_count = [2,2,2,2]
        self.round_card_put = [None for i in range(14)] 
        self.basic_card_put = [None for i in range(16)]
    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def set_now_round(self, now_round):
        self.now_round = now_round
        self.notify()

    def set_now_turn_player(self, now_turn_player):
        self.now_turn_player = now_turn_player
        self.notify()

    def set_next_turn_player(self, next_turn_player):
        self.next_turn_player = next_turn_player
        self.notify()

    def set_round_resource(self, index, value):
        self.round_resource[index] = value
        self.notify()

    def set_round_card_order(self, index, value):
        self.round_card_order[index] = value
        self.notify()

    def set_basic_resource(self, index, value):
        self.basic_resource[index] = value
        self.notify()



    def get_sheep_card_index(self):
        for i, num in enumerate(self.round_card_order):
            if num is RoundBehaviorType.SHEEP1.value:
                return i

    def get_cow_card_index(self):
        for i, num in enumerate(self.round_card_order):
            if num is RoundBehaviorType.COW.value:
                return i

    def get_pig_card_index(self):
        for i, num in enumerate(self.round_card_order):
            if num is RoundBehaviorType.PIG.value:
                return i

    def get_stone2_card_index(self):
        for i, num in enumerate(self.round_card_order):
            if num is RoundBehaviorType.STONE_2.value:
                return i

    def get_stone4_card_index(self):
        for i, num in enumerate(self.round_card_order):
            if num is RoundBehaviorType.STONE_4.value:
                return i


