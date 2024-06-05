"""
게임 전체의 진행 상태를 저장하는 클래스
"""


class GameStatus:
    def __init__(self):
        self.observers = []
        self.now_round = 0          # 현재 라운드
        self.now_turn_player = 0    # 현재 턴 플레이어
        self.next_turn_player = 0   # 다음 턴 플레이어
        self.round_card_order = [[i for i in range(0, 4)],
                                 [i for i in range(4, 7)],
                                 [i for i in range(7, 9)],
                                 [i for i in range(9, 11)],
                                 [i for i in range(11, 13)],
                                 [i for i in range(13, 14)]]
        self.round_resource = [0 for i in range(14)]
        self.basic_resource = [0 for i in range(16)]

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def set_now_round(self, round):
        self.now_round = round
        self.notify()

    def set_round_resource(self, index, value):
        self.round_resource[index] = value
        self.notify()

    def set_basic_resource(self, index, value):
        self.basic_resource[index] = value
        self.notify()