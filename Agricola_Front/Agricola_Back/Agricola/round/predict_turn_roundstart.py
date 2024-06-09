from command import Command
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


class PredictTurnRoundStart(Command):
    def execute(self):
        for i in range(4):
            if player_status_repository.player_status[i].resource.first_turn:
                game_status_repository.game_status.next_turn_player = i

    def log(self):
        pass