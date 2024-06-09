"""
외양간 설치 커맨드
3*5 0-indexed 기준 포지션을 입력받아 해당 위치에 외양간을 건설하고, 해당 외양간의 영향을 받는 모든 위치의 maximum 값을 조절한다.

"""
from collections import deque
from typing import List

from command import Command
from entity.farm.field import Field
from entity.farm.none_field import NoneField
from entity.field_type import FieldType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


class CreateBarn(Command):
    def __init__(self, field_status, vertical_fence, horizontal_fence, position):
        self.field_status = field_status
        self.vertical_fence = vertical_fence
        self.horizontal_fence = horizontal_fence
        self.position = position

    def execute(self):
        if isinstance(self.field_status[self.position[0]][self.position[1]], NoneField):
            self.field_status[self.position[0]][self.position[1]].barn = True
            self.field_status[self.position[0]][self.position[1]].maximum = 1
            player_status_repository.player_status[game_status_repository.game_status.now_turn_player].farm.field[self.position[0]][self.position[1]] \
                = self.field_status[self.position[0][self.position[1]]]
            return True
        expanded_field: List[List[Field]] = [[NoneField() for i in range(13)] for i in range(9)]
        for i in range(3):
            for j in range(6):
                if self.vertical_fence is True:
                    expanded_field[i * 2 + 2][2 * j + 1].field_type = FieldType.FENCE
        for i in range(4):
            for j in range(5):
                if self.horizontal_fence is True:
                    expanded_field[i * 2 + 1][j * 2 + 2].field_type = FieldType.FENCE
        for i in range(3):
            for j in range(5):
                expanded_field[i * 2 + 3][j * 2 + 3] = self.field_status[i][j]
        queue = deque()
        check = [[False for _ in range(13)] for __ in range(9)]
        queue.append((self.position[0]*2 + 3, self.position[1]*2 + 3))
        check[self.position[0]*2 + 3][self.position[1] * 2 + 3] = True
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        expanded_field[self.position[0]*2 + 3][self.position[1]*2 + 3].maximum *= 2
        while not queue:
            x, y = queue.popleft()
            for k in range(4):
                p = x + dx[k] + dx[k]
                q = y + dy[k] + dy[k]
                pp = x + dx[k]
                qq = y + dy[k]
                if 0 <= p < 9 and 0 <= q < 13 and expanded_field[pp][qq].field_type != FieldType.FENCE and not \
                check[p][q]:
                    check[p][q] = True
                    expanded_field[p][q].maximum *= 2
                    queue.append((p, q))

        field_status = [[Field() for _ in range(5)] for __ in range(3)]
        for i in range(3):
            for j in range(5):
                field_status[i][j] = expanded_field[i*2 + 2][j * 2 + 2]
        player_status_repository.player_status[game_status_repository.game_status.now_turn_player].farm.field = field_status
        return True

    def log(self):
        pass
