"""
게임판을 정리하는 커맨드
"""
from command import Command
from repository.round_status_repository import round_status_repository


class CleanGameBoard(Command):
    def execute(self):
        round_status = round_status_repository.round_status
        for i in range(16):
            round_status.put_basic[i] = -1
        for i in range(14):
            round_status.put_round[i] = -1

    def log(self):
        pass
