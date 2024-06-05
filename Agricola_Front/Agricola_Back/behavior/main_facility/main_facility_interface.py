"""
주요 설비 인터페이스
"""
from abc import abstractmethod
from command import Command


class MainFacilityInterface(Command):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def log(self):
        pass

    @abstractmethod
    def purchase(self):
        pass

    @abstractmethod
    def canUse(self):
        pass