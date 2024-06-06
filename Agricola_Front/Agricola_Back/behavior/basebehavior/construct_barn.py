"""
외양간 짓기 기초 행동
:param: 플레이어 번호, 변경하고자 하는 필드 상태
:return: 집 확장 성공 여부 반환
:rtype: bool
농장 상태 업데이트도 수행되어야 함.
"""

from behavior.basebehavior.house_expansion import *
from entity.field_type import FieldType


class ConstructBarn(Command):

    def __init__(self, barn_index, field_status):
        self.log_text = None
        self.barn_index = barn_index
        self.field_status = field_status

    def execute(self):
        barn_cnt = 0
        for row in self.field_status:
            for element in row:
                if element.barn:
                    barn_cnt += 1
        selected_field_type = self.field_status[self.barn_index[0]][self.barn_index[1]]
        if barn_cnt == 4 or selected_field_type != FieldType.CAGE:
            self.log_text = "외양간 건설 검증에 실패할 수 없습니다"
            return False
        else:
            self.log_text = "외양간 위치 검증에 성공했습니다"
            return True

    def log(self):
        return self.log_text
