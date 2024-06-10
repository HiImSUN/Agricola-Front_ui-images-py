"""
빵 굽기 함수
빵 굽기 가능 여부 ->
"""
from behavior.basebehavior.base_behavior_interface import BaseBehaviorInterface
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from behavior.main_facility.dirt_kiln import DirtKiln
from behavior.main_facility.oven1 import Oven1
from behavior.main_facility.oven2 import Oven2
from behavior.main_facility.strong_oven1 import StrongOven1
from behavior.main_facility.strong_oven2 import StrongOven2


class DoBake(BaseBehaviorInterface):
    def __init__(self, cookValue):
        self.log_text = ""
        self.game_status = game_status_repository.game_status
        self.player_resource = player_status_repository.player_status[
            game_status_repository.game_status.now_turn_player].resource
        self.player_MainCard = player_status_repository.player_status[
            game_status_repository.game_status.now_turn_player].card.putMainCard
        self.cookValue = cookValue  # 구울 양

    def execute(self):
        leftBake = self.cookValue
        if any(isinstance(card, DirtKiln) for card in self.player_MainCard):
            leftBake -= 1
            self.player_resource.set_food(self.player_resource.food + 5)
        elif any(isinstance(card, (StrongOven1, StrongOven2)) for card in self.player_MainCard):
            self.player_resource.set_food(self.player_resource.food + leftBake * 3)
            leftBake = 0
        elif any(isinstance(card, (Oven1, Oven2)) for card in self.player_MainCard):
            self.player_resource.set_food(self.player_resource.food + leftBake * 2)
            leftBake = 0
        if (leftBake != 0):
            self.log_text = f"주요 설비 부족으로 곡식 {leftBake}개를 굽지 못했습니다"
            return False
        self.log_text = "빵 굽기를 완료했습니다"
        return True

    def log(self):
        return self.log_text

    def can_play(self):
        if not self.player_MainCard:
            return False
        else:
            return True
