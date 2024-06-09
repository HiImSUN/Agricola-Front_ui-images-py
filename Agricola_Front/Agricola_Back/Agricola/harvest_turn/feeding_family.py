"""
가족 먹여살리기
"""
from command import Command
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


class FeedingFamily(Command):
    def execute(self):
        need = player_status_repository.player_status[game_status_repository.game_status.now_turn_player].worker * 3
        need += player_status_repository.player_status[game_status_repository.game_status.next_turn_player].baby
        player_status_repository.player_status[game_status_repository.game_status.now_turn_player].resource.food -= need
        if player_status_repository.player_status[game_status_repository.game_status.now_turn_player].resource.food < 0:
            beg = -player_status_repository.player_status[game_status_repository.game_status.now_turn_player].resource.food
            player_status_repository.player_status[game_status_repository.game_status.now_turn_player].resource.food = 0
            player_status_repository.player_status[game_status_repository.game_status.now_turn_player].resource.beg_token += beg
            return beg
        return 0

    def log(self):
        pass
