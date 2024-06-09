"""
외양간 짓기 기초 행동
:param: 변경하고자 하는 필드 상태 (3*5 field 객체 배열), vertical fence 상태, horizontal fence 상태
:return: 집 확장 성공 여부 반환
:rtype: bool
농장 상태 업데이트도 수행되어야 함.
"""
import copy

from behavior.unitbehavior.create_barn import CreateBarn
from behavior.basebehavior.house_expansion import *
from entity.field_type import FieldType


class ConstructBarn(BaseBehaviorInterface):

    def __init__(self, field_status, vertical_fence, horizontal_fence, barn_index):
        self.log_text = ""
        self.field_status = copy.deepcopy(field_status)
        self.vertical_fence = copy.deepcopy(vertical_fence)
        self.horizontal_fence = copy.deepcopy(horizontal_fence)
        self.barn_index = barn_index

    def execute(self):
        barn_cnt = 0
        for row in self.field_status:
            for element in row:
                if element.barn:
                    barn_cnt += 1
        selected_field_type = self.field_status[self.barn_index[0]][self.barn_index[1]]
        if barn_cnt >= 4 or selected_field_type != FieldType.CAGE:
            self.log_text = "외양간 건설이 불가능합니다."
            return False
        elif player_status_repository.player_status[game_status_repository.game_status.now_turn_player].resource.wood < 2:
            self.log_text = "나무가 모자랍니다."
            return False
        else:
            if not CreateBarn(self.field_status, self.vertical_fence, self.horizontal_fence, self.barn_index):
                self.log_text = ""
                return False

            self.log_text = "외양간 건설 완료"
            player_status_repository.player_status[game_status_repository.game_status.now_turn_player].resource.wood -= 2
            return True

    def log(self):
        return self.log_text
