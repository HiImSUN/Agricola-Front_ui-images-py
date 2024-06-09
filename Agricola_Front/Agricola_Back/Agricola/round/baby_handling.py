"""
신생아 처리 커맨드
"""
from command import Command
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


class BabyHandling(Command):
    def execute(self):
        now_turn_player = game_status_repository.game_status.now_turn_player
        now_turn_player_status = player_status_repository.player_status[now_turn_player]
        now_turn_player_status.set_worker(now_turn_player_status.worker + now_turn_player_status.baby)
        now_turn_player_status.set_baby(0)

    def log(self):
        return "아이가 성장했습니다."