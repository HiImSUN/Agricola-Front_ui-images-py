def fence_validation():
    field_status = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]
    log = []

    def check_fence_form():
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for i, item in enumerate(field_status):
            for j, value in enumerate(item):
                if i % 2 == 0 and j % 2 == 0:
                    adjacent = 0
                    for k in range(4):
                        p = i + dx[k]
                        q = j + dy[k]
                        if p < 0 or q < 0 or p >= 7 or q >= 11:
                            continue
                        if field_status[p][q] == FieldType.FENCE:
                            adjacent += 1
                    if adjacent == 1:
                        log.append("울타리의 형식이 올바르지 않습니다.")
                        return False
        return True

    def check_connected_component_fence():
        expanded_field_status = [[FieldType.NONE_FIELD for i in range(13)]for j in range(9)]
        check = [[0 for i in range(13)]for j in range(9)]
        for i, item in enumerate(field_status):
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
            log.append("울타리는 하나로 이어져 있어야 합니다.")
            return False
        else:
            return True
        
    def check_inside_object():
        expanded_field_status = [[FieldType.NONE_FIELD for i in range(13)]for j in range(9)]
        check = [[0 for i in range(13)]for j in range(9)]
        for i, item in enumerate(field_status):
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
                    log.append("울타리 안에는 외양간을 제외한 다른 구조물이 있을 수 없습니다.")
                    return False
        return True

    def check_fence_count():
        cnt = 0
        for fence in field_status:
            for value in fence:
                if value == FieldType.FENCE:
                    cnt += 1
        if cnt <= 15:
            return True
        else:
            log.append("울타리의 최대 설치 가능 개수는 15개 입니다.")
            return False

    return ( check_fence_form() and check_connected_component_fence() and check_inside_object() and check_fence_count() ), log

def execute(self):
    player_status = self.player_status
    game_status = self.game_status
    field_status = player_status[self.game_status.now_turn_player].farm.field
    vertical_fence = player_status[self.game_status.now_turn_player].farm.vertical_fence
    horizontal_fence = player_status[self.game_status.now_turn_player].farm.horizon_fence

    expanded_field = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]
    for i in range(3):
        for j in range(6):
            if vertical_fence is True:
                expanded_field[i * 2 + 1][2 * j] = FieldType.FENCE
    for i in range(4):
        for j in range(5):
            if horizontal_fence is True:
                expanded_field[i * 2][j * 2 + 1] = FieldType.FENCE
    for i in range(3):
        for j in range(5):
            expanded_field[i * 2 + 1][j * 2 + 1] = field_status[i][j].field_type
    fence_validation = FenceValidation(expanded_field)
    if fence_validation.execute():
        cost = 0
        for i in range(4):
            for j in range(5):
                if horizontal_fence is True and player_status[game_status.now_turn_player].farm.horizon_fence[i][j] is False:
                    cost += 1
        for i in range(3):
            for j in range(6):
                if vertical_fence is True and player_status[game_status.now_turn_player].farm.vertical_fence[i][j] is False:
                    cost += 1
        if cost > player_status[game_status.now_turn_player].resource.wood:
            log_text = "나무가 모자랍니다."
            return False
        if not CreateCage(field_status, vertical_fence, horizontal_fence):
            log_text = "잘못된 동물 배치"
            return False
        player_status[game_status.now_turn_player].resource.wood -= cost
        log_text = "울타리 건설 성공"
        return True
    else:
        log_text = "울타리 건설 검증에 실패했습니다"
        return False