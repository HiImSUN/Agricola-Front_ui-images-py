"""
플레이어 상태 저장소
"""
from entity.player_status import PlayerStatus


class PlayerStatusRepository:
    def __init__(self):
        self.player_status = [PlayerStatus() for i in range(4)] 
        
player_status_repository = PlayerStatusRepository()