"""
경작지 확장 검증 클래스
:param: 3*5 필드 객체 배열을 입력으로 받는다.
:return: 올바른 경작지의 형태를 띄고 있는지 여부를 T/F값으로 반환한다.
:rtype: bool
Unit : 준영
"""
from collections import deque
from copy import copy

from command import Command
from entity.field_type import FieldType


def check_connected_component(field_status, field_type):
    ret = 0
    queue = deque()
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    check = [[0 for i in range(5)] for j in range(3)]
    for i, fields in enumerate(field_status):
        for j, field in enumerate(fields):
            if field.field_type == field_type and check[i][j] == 0:
                ret += 1
                check[i][j] = 1
                queue.append((i, j))
                while queue:
                    item = queue.popleft()
                    for k in range(4):
                        nx = item[0] + dx[k]
                        ny = item[1] + dy[k]
                        if 3 > nx >= 0 == check[nx][ny] and 0 <= ny < 5 and field.field_type == field_type:
                            check[nx][ny] = 1
                            queue.append((nx, ny))
    return ret


class ArableExpandValidation(Command):
    def __init__(self, field_status):
        self.field_status = copy(field_status)
        self.log_text = None

    def execute(self):
        val = check_connected_component(field_status=self.field_status, field_type=FieldType.ARABLE)
        if val <= 1:
            self.log_text = "올바른 경작지 배치."
            return True
        else:
            self.log_text = "올바르지 않은 경작지 배치 : 경작지는 하나로 모여있어야 합니다."
            return False

    def log(self):
        return self.log_text


"""
경작지 확장의 검증
1. 경작지가 하나의 연결 요소로 이루어져 있어야 한다.

"""
