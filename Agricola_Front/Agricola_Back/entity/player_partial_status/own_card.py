"""
현재 해당 플레이어가 사용할 수 있는 카드들에 대한 정보
"""


class OwnCard:
    def __init__(self):
        self.observers = []
        self.handSubCard = []
        self.handJobCard = []
        self.putSubCard = []
        self.putJobCard = []
        self.putMainCard = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def set_hand_sub_card(self, hand_sub_card):
        self.handSubCard = hand_sub_card
        self.notify()

    def set_hand_job_card(self, hand_job_card):
        self.handJobCard = hand_job_card
        self.notify()

    def set_put_sub_card(self, put_sub_card):
        self.putSubCard = put_sub_card
        self.notify()

    def set_put_job_card(self, put_job_card):
        self.putJobCard = put_job_card
        self.notify()

    def set_put_main_card(self, put_main_card):
        self.putMainCard = put_main_card
        self.notify()