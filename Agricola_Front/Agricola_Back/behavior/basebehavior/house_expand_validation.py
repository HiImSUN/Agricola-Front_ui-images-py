"""
집 확장 검증 클래스
Unit : 홍규
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
                        if 3 > nx >= 0 and 0 <= ny < 5 and check[nx][ny] == 0 and field.field_type == field_type:
                            check[nx][ny] = 1
                            queue.append((nx, ny))
    return ret


class HouseExpandValidation(Command):
    def __init__(self, field_status):
        self.field_status = copy(field_status)
        self.log_text = None

    def execute(self):
        val = check_connected_component(field_status=self.field_status, field_type=FieldType.HOUSE)
        if val <= 1:
            self.log_text = "올바른 집 배치."
            return True
        else:
            self.log_text = "올바르지 않은 집 배치 : 집은 하나로 모여있어야 합니다."
            return False

    def log(self):
        return self.log_text
