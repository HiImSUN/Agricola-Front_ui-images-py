import random

from command import Command
from repository.game_status_repository import game_status_repository


class RoundCardShuffle(Command):
    def execute(self):
        weeks = [
            random.sample(range(0, 4), 4),
            random.sample(range(4, 7), 3),
            random.sample(range(7, 9), 2),
            random.sample(range(9, 11), 2),
            random.sample(range(11, 13), 2),
            random.sample(range(13, 14), 1)
        ]

        offsets = [0, 4, 7, 9, 11, 13]

        for week, offset in zip(weeks, offsets):
            for i, source in enumerate(week):
                game_status_repository.game_status.set_round_card_order(i + offset, source)

    def log(self):
        pass
