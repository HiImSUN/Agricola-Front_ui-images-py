"""
게임 시작 후 초기 자원 분배 커맨드
"""
from command import Command
from repository.player_status_repository import player_status_repository


class StartResourceDistribution(Command):
    def execute(self):
        player_status_repository.player_status[0].resource.set_food(3)
        player_status_repository.player_status[0].resource.set_first_turn(True)
        player_status_repository.player_status[0].set_worker(2)
        player_status_repository.player_status[1].resource.set_food(4)
        player_status_repository.player_status[1].set_worker(2)
        player_status_repository.player_status[2].resource.set_food(4)
        player_status_repository.player_status[2].set_worker(2)
        player_status_repository.player_status[3].resource.set_food(4)
        player_status_repository.player_status[3].set_worker(2)

    def log(self):
        pass