"""
울타리 + 우리 생성 클래스
:param: 변경하고자 하는 필드 상태 (3*5 field), vertical fence 상태, horizontal fence 상태
:return: 우리 생성 성공 여부
:rtype: bool
우리 생성 및 max 값 조정
농장 상태 업데이트도 수행되어야 함
"""
import copy

from behavior.basebehavior.base_behavior_interface import BaseBehaviorInterface
from behavior.unitbehavior.create_cage import CreateCage
from entity.field_type import FieldType
from behavior.validation.fence_validation import FenceValidation
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


class ConstructFence(BaseBehaviorInterface):

    def __init__(self, field_status, vertical_fence, horizontal_fence):
        self.field_status = copy.deepcopy(field_status)
        self.vertical_fence = copy.deepcopy(vertical_fence)
        self.horizontal_fence = copy.deepcopy(horizontal_fence)
        self.log_text = ""

    def execute(self):
        expanded_field = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]
        for i in range(3):
            for j in range(6):
                if self.vertical_fence is True:
                    expanded_field[i * 2 + 1][2 * j] = FieldType.FENCE
        for i in range(4):
            for j in range(5):
                if self.horizontal_fence is True:
                    expanded_field[i * 2][j * 2 + 1] = FieldType.FENCE
        for i in range(3):
            for j in range(5):
                expanded_field[i * 2 + 1][j * 2 + 1] = self.field_status[i][j].field_type
        fence_validation = FenceValidation(expanded_field)
        if fence_validation.execute():
            cost = 0
            for i in range(4):
                for j in range(5):
                    if self.horizontal_fence is True and player_status_repository.player_status[ \
                            game_status_repository.game_status.now_turn_player].farm.horizon_fence[i][j] is False:
                        cost += 1
            for i in range(3):
                for j in range(6):
                    if self.vertical_fence is True and player_status_repository.player_status[ \
                            game_status_repository.game_status.now_turn_player].farm.vertical_fence[i][j] is False:
                        cost += 1
            if cost > player_status_repository.player_status[
                game_status_repository.game_status.now_turn_player].resource.wood:
                self.log_text = "나무가 모자랍니다."
                return False
            if not CreateCage(self.field_status, self.vertical_fence, self.horizontal_fence):
                self.log_text = "잘못된 동물 배치"
                return False
            player_status_repository.player_status[
                game_status_repository.game_status.now_turn_player].resource.wood -= cost
            self.log_text = "울타리 건설 성공"
            return True
        else:
            self.log_text = "울타리 건설 검증에 실패했습니다"
            return False

    def log(self):
        return self.log_text
