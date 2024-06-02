"""
게임 상태 저장소
"""
from entity.game_status import GameStatus


class GameStatusRepository:
    def __init__(self):
        self.game_status = GameStatus()
    
game_status_repository = GameStatusRepository()
