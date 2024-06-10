from command import Command
from repository.game_status_repository import game_status_repository


class CheckHarvestTurnRemain(Command):
    def execute(self):
        if game_status_repository.game_status.next_turn_player == 4:
            game_status_repository.game_status.next_turn_player = -1

    def log(self):
        pass
