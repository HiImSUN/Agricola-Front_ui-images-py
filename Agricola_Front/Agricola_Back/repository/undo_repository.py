"""
undo 를 위한 현재 상태 저장소
"""
from entity.game_status import GameStatus
from entity.player_status import PlayerStatus
from entity.round_status import RoundStatus

import copy


class UndoRepository:
    def __init__(self, game_status: GameStatus, player_status: PlayerStatus, round_status: RoundStatus):
        self.game_status = copy.deepcopy(game_status)
        self.player_status = copy.deepcopy(player_status)
        self.round_status = copy.deepcopy(round_status)

    def undo(self):
        # Todo
        pass