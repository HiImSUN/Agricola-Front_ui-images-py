"""
라운드 상태 저장소
"""
from entity.round_status import RoundStatus


class RoundStatusRepository:
    def __init__(self):
        self.round_status = RoundStatus()


round_status_repository = RoundStatusRepository()