"""
플레이어의 상태 저장 엔티티
"""
from entity.farm.farm import Farm
from entity.player_partial_status.own_card import OwnCard
from entity.player_partial_status.resource import Resource
from entity.round_status import RoundStatus

from entity.farm.farm import Farm
from entity.player_partial_status.own_card import OwnCard
from entity.player_partial_status.resource import Resource


class PlayerStatus:
    def __init__(self):
        self.observers = []
        self.card = OwnCard()
        self.farm = Farm()
        self.resource = Resource()
        self.worker = 0
        self.baby = 0
        self.score = 0

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def set_worker(self, worker):
        self.worker = worker
        self.notify()

    def set_baby(self, baby):
        self.baby = baby
        self.notify()

    def set_card(self, card):
        self.card = card
        self.notify()
