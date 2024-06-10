from abc import abstractmethod

from command import Command


class BaseBehaviorInterface(Command):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def log(self):
        pass

    def can_play(self):
        return True

