"""
집 확장(새 방 만들기) 기초 행동
:param: 플레이어 번호, 변경하고자 하는 필드 상태
:return: 집 확장 성공 여부 반환
:rtype: bool
농장 상태 업데이트도 수행되어야 함.
"""
from copy import deepcopy

from behavior.basebehavior.base_behavior_interface import BaseBehaviorInterface
from entity.house_type import HouseType
from behavior.validation.house_expand_validation import HouseExpandValidation
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


class HouseExpansion(BaseBehaviorInterface):

    def __init__(self, field_status):
        self.field_status = deepcopy(field_status)
        self.log_text = ""

    def execute(self):
        checkValidation = HouseExpandValidation(self.field_status)
        if checkValidation.execute():
            self.log_text = "농장을 확장하는데 성공했습니다."
            player_status_repository.player_status[game_status_repository.game_status.now_turn_player].farm.field = self.field_status
            return True
        else:
            self.log_text = "농장 확장 검증에 실패했습니다"
            return False

    def log(self):
        return self.log_text

    def can_play(self):
        if player_status_repository.player_status[game_status_repository.game_status.now_turn_player].resource.reed >= 2:
            if player_status_repository.player_status[game_status_repository.game_status.now_turn_player].farm.house_status == HouseType.WOOD \
                and player_status_repository.player_status[game_status_repository.game_status.now_turn_player].resource.dirt >= 5:
                return True
            if player_status_repository.player_status[game_status_repository.game_status.now_turn_player].farm.house_status == HouseType.DIRT \
                and player_status_repository.player_status[game_status_repository.game_status.now_turn_player].resource.stone >= 5:
                return True
        self.log_text = "자원이 모자랍니다."
        return False
