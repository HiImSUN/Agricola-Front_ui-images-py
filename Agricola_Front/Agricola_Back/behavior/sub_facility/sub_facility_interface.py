"""
보조 설비 카드 행동 인터페이스
"""
from abc import abstractmethod

from command import Command


class SubFacilityInterface(Command):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def log(self):
        pass

    @abstractmethod
    def putDown(self):
        pass

    @abstractmethod
    def canUse(self):
        pass