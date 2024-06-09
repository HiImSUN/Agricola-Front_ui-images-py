from abc import abstractmethod, ABC

from command import Command


class BehaviorInterface(Command, ABC):
    def can_play(self):
        return True
