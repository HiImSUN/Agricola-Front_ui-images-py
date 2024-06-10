"""
턴이 남아있는지 체크하는 커맨드
"""
from command import Command
from repository.game_status_repository import game_status_repository
from repository.round_status_repository import round_status_repository


class CheckTurnRemain(Command):
    def execute(self):
        for i in range(4):
            if round_status_repository.round_status.remain_workers[i] > 0:
                return
        game_status_repository.game_status.set_next_turn_player(-1)

    def log(self):
        pass