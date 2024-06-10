"""
undo point 를 저장하는 커맨드
"""
from command import Command
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository
from repository.undo_repository import undo_repository


class SaveUndoPoint(Command):
    def execute(self):
        undo_repository.save(game_status_repository.game_status, player_status_repository.player_status, round_status_repository.round_status)

    def log(self):
        pass