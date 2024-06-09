"""
현재 해당 플레이어가 사용할 수 있는 카드들에 대한 정보
모든 카드들의 정보는 커맨드 클래스 생성자로 저장된다.
"""


class OwnCard:
    def __init__(self):
        self.observers = []
        self.hand_sub_card = []
        self.hand_job_card = []
        self.put_sub_card = []
        self.put_job_card = []
        self.put_main_card = []
        self.start_job_card = []
        self.start_sub_card = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def add_hand_sub_card(self, hand_sub_card):
        self.hand_sub_card.append(hand_sub_card)
        self.notify()

    def add_hand_job_card(self, hand_job_card):
        self.hand_job_card.append(hand_job_card)
        self.notify()

    def add_put_sub_card(self, put_sub_card):
        self.put_sub_card.append(put_sub_card)
        self.notify()

    def add_put_job_card(self, put_job_card):
        self.put_job_card.append(put_job_card)
        self.notify()

    def add_put_main_card(self, put_main_card):
        self.put_main_card.append(put_main_card)
        self.notify()