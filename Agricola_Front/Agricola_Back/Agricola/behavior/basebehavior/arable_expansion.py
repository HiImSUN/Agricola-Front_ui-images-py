"""
밭 1개 일구기 기초 행동
:param: 필드 상태 (3*5 필드 객체 배열)
:return: 밭 1개 일구기 성공 여부
:rtype: bool
실제 밭 정보를 업데이트한다.
"""
import copy

from behavior.basebehavior.base_behavior_interface import BaseBehaviorInterface
from behavior.validation.arable_expand_validation import ArableExpandValidation
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


class ArableExpansion(BaseBehaviorInterface):

    def __init__(self, field_status):
        self.field_status = copy.deepcopy(field_status)
        self.log_text = ""

    def execute(self):
        check_validation = ArableExpandValidation(self.field_status)
        if check_validation.execute():
            self.log_text = "밭 일구기 검증에 성공했습니다"
            player_status_repository.player_status[game_status_repository.game_status.now_turn_player].farm.field = self.field_status
            return True
        else:
            self.log_text = "밭 일구기 검증에 실패했습니다"
            return False

    def log(self):
        return self.log_text
