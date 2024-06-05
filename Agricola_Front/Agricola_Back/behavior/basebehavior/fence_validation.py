"""
울타리 검증 클래스
:param list:  7 * 11 의 enum으로 채워진 필드 상태 배열
:return: 올바른 울타리 여부.
Unit : 준호
"""
from collections import deque
from copy import copy

from command import Command
from entity.field_type import FieldType


class FenceValidation(Command):
    def __init__(self, field_status):
        self.field_status = copy(field_status)
        self.log_text = None

    def execute(self):
        return self.check_fence_form() and self.check_connected_component_fence() and self.check_inside_object() and self.check_fence_count()

    def check_fence_form(self):
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for i, item in enumerate(self.field_status):
            for j, value in enumerate(item):
                if i % 2 == 0 and j % 2 == 0:
                    adjacent = 0
                    for k in range(4):
                        p = i + dx[k]
                        q = j + dy[k]
                        if p < 0 or q < 0 or p >= 7 or q >= 11:
                            continue
                        if self.field_status[p][q] == FieldType.FENCE:
                            adjacent += 1
                    if adjacent is 1:
                        self.log_text = "울타리의 형식이 올바르지 않습니다."
                        return False
        return True

    def check_connected_component_fence(self):
        expanded_field_status = [[FieldType.NONE_FIELD for i in range(13)]for j in range(9)]
        check = [[0 for i in range(13)]for j in range(9)]
        for i, item in enumerate(self.field_status):
            for j, value in enumerate(item):
                expanded_field_status[i+1][j+1] = value
        queue = deque()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        check[0][0] = 1
        queue.append((0, 0))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                p = x + dx[i]
                q = y + dy[i]
                r = p + dx[i]
                s = q + dy[i]
                if 0 <= r < 9 and 0 <= s < 13 and check[r][s] == 0 and expanded_field_status[p][q] != FieldType.FENCE:
                    check[r][s] = 1
                    queue.append((r, s))
        ret = 0
        for i in range(0, 9, 2):
            for j in range(0, 13, 2):
                if (expanded_field_status[i][j] == FieldType.CAGE or expanded_field_status[i][j] == FieldType.NONE_FIELD) \
                        and check[i][j] == 0:
                    ret += 1
                    check[i][j] = 1
                    queue.append((i, j))
                    while queue:
                        item = queue.popleft()
                        for k in range(4):
                            nx = item[0] + dx[k] + dx[k]
                            ny = item[1] + dy[k] + dy[k]
                            if 9 > nx >= 0 == check[nx][ny] and 0 <= ny < 13:
                                check[nx][ny] = 1
                                queue.append((nx, ny))
        if ret > 1:
            self.log_text = "울타리는 하나로 이어져 있어야 합니다."
            return False
        else:
            return True

    def check_inside_object(self):
        expanded_field_status = [[FieldType.NONE_FIELD for i in range(13)]for j in range(9)]
        check = [[0 for i in range(13)]for j in range(9)]
        for i, item in enumerate(self.field_status):
            for j, value in enumerate(item):
                expanded_field_status[i+1][j+1] = value
        queue = deque()
        check[0][0] = 1
        queue.append((0, 0))
        while queue:
            x, y = queue.popleft()
            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]
            for i in range(4):
                p = x + dx[i]
                q = y + dy[i]
                r = p + dx[i]
                s = q + dy[i]
                if 0 <= r < 9 and 0 <= s < 13 and check[r][s] == 0 and expanded_field_status[p][q] != FieldType.FENCE:
                    check[r][s] = 1
                    queue.append((r, s))
        for i in range(0, 9, 2):
            for j in range(0, 13, 2):
                if check[i][j] == 0 and expanded_field_status[i][j] != FieldType.NONE_FIELD \
                        and expanded_field_status[i][j] != FieldType.CAGE:
                    self.log_text = "울타리 안에는 외양간을 제외한 다른 구조물이 있을 수 없습니다."
                    return False
        return True

    def check_fence_count(self):
        cnt = 0
        for fence in self.field_status:
            for value in fence:
                if value == FieldType.FENCE:
                    cnt += 1
        if cnt <= 15:
            return True
        else:
            self.log_text = "울타리의 최대 설치 가능 개수는 15개 입니다."
            return False

    def log(self):
        return self.log_text


"""
1. 울타리 형태
    - 울타리는 양 끝이 다른 울타리로 이어져 있어야 한다
    - 우리는 붙어있어야 한다
2. 내부 요소 여부 (외양간 제외)
3. 울타리 갯수
"""