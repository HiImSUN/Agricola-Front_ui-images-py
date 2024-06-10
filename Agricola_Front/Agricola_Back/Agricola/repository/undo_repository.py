"""
undo 를 위한 현재 상태 저장소
"""
from entity.game_status import GameStatus
from entity.player_status import PlayerStatus
from entity.round_status import RoundStatus

import copy

from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository


class UndoRepository:

    def __init__(self):
        self.round_status = None
        self.player_status = None
        self.game_status = None

    def undo(self):
        game_status_repository.game_status = self.game_status
        player_status_repository.player_status = self.player_status
        round_status_repository.round_status = self.round_status
        self.save(self.game_status, self.player_status, self.round_status)

    def save(self, game_status: GameStatus, player_status: PlayerStatus, round_status: RoundStatus):
        self.game_status = copy.deepcopy(game_status)
        self.player_status = copy.deepcopy(player_status)
        self.round_status = copy.deepcopy(round_status)


undo_repository = UndoRepository()
