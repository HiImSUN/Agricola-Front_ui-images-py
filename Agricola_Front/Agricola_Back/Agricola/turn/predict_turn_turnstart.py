from command import Command
from repository.game_status_repository import game_status_repository
from repository.round_status_repository import round_status_repository


class PredictTurnTurnStart(Command):
    def execute(self):
        for i in range(1, 5):
            if round_status_repository.round_status.remain_workers[(game_status_repository.game_status.now_turn_player + i)%4] > 0:
                game_status_repository.game_status.set_next_turn_player((game_status_repository.game_status.now_turn_player + i)%4)

    def log(self):
        pass