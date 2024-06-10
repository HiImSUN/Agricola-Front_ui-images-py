"""
상태 패턴 추상 클래스
"""
from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, game_context):
        self.game_context = game_context

    @abstractmethod
    def next_state(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    def log(self):
        pass


