import random
from copy import deepcopy
from collections import deque
from copy import copy

# from command import Command
# from entity.field_type import FieldType
from Agricola_Back.Agricola.behavior.job.greengrocer import Greengrocer
from Agricola_Back.Agricola.behavior.job.hedger import Hedger
from Agricola_Back.Agricola.behavior.job.kiln_baker import KilnBaker
from Agricola_Back.Agricola.behavior.job.livestock_dealer import LivestockDealer
from Agricola_Back.Agricola.behavior.job.lumberjack import Lumberjack
from Agricola_Back.Agricola.behavior.job.magician import Magician
from Agricola_Back.Agricola.behavior.job.priest import Priest
from Agricola_Back.Agricola.behavior.job.roofer import Roofer
from Agricola_Back.Agricola.behavior.job.skilled_bricklayer import SkilledBrickLayer
from Agricola_Back.Agricola.behavior.job.small_farmer import SmallFarmer
from Agricola_Back.Agricola.behavior.job.sub_cultivator import SubCultivator
from Agricola_Back.Agricola.behavior.job.warehouse_manager import WarehouseManager
from Agricola_Back.Agricola.behavior.sub_facility.basket import Basket
from Agricola_Back.Agricola.behavior.sub_facility.bottle import Bottle
from Agricola_Back.Agricola.behavior.sub_facility.canoe import Canoe
from Agricola_Back.Agricola.behavior.sub_facility.giant_farm import GiantFarm
from Agricola_Back.Agricola.behavior.sub_facility.grain_shovel import GrainShovel
from Agricola_Back.Agricola.behavior.sub_facility.junk_warehouse import JunkWarehouse
from Agricola_Back.Agricola.behavior.sub_facility.loam_mining_site import LoamMiningSite
from Agricola_Back.Agricola.behavior.sub_facility.manger import Manger
from Agricola_Back.Agricola.behavior.sub_facility.pincer import Pincer
from Agricola_Back.Agricola.behavior.sub_facility.pitchfork import Pitchfork
from Agricola_Back.Agricola.behavior.sub_facility.silpan import SilPan
from Agricola_Back.Agricola.behavior.sub_facility.wool_blanket import WoolBlanket
from Agricola_Back.Agricola.behavior.basebehavior.construct_fence import ConstructFence
from Agricola_Back.Agricola.entity.field_type import FieldType

def RoundCardShuffle(self):
        weeks = [
            random.sample(range(0, 4), 4),
            random.sample(range(4, 7), 3),
            random.sample(range(7, 9), 2),
            random.sample(range(9, 11), 2),
            random.sample(range(11, 13), 2),
            random.sample(range(13, 14), 1)
        ]

        offsets = [0, 4, 7, 9, 11, 13]

        for week, offset in zip(weeks, offsets):
            for i, source in enumerate(week):
                self.game_status.set_round_card_order(i + offset, source)

def StartResourceDistribution(self):
    self.player_status[0].resource.set_food(3)
    self.player_status[0].resource.set_first_turn(True)
    self.player_status[0].set_worker(2)
    self.player_status[1].resource.set_food(4)
    self.player_status[1].set_worker(2)
    self.player_status[2].resource.set_food(4)
    self.player_status[2].set_worker(2)
    self.player_status[3].resource.set_food(4)
    self.player_status[3].set_worker(2)
def CardDistribution(self):
    sub_card_list = random.sample(range(12), 12)
    for i in range(4):
        for j in range(3):
            if sub_card_list[i * 3 + j] == 0:
                self.player_status[i].card.hand_sub_card.append(Basket)
            if sub_card_list[i * 3 + j] == 1:
                self.player_status[i].card.hand_sub_card.append(Bottle)
            if sub_card_list[i * 3 + j] == 2:
                self.player_status[i].card.hand_sub_card.append(Canoe)
            if sub_card_list[i * 3 + j] == 3:
                self.player_status[i].card.hand_sub_card.append(GiantFarm)
            if sub_card_list[i * 3 + j] == 4:
                self.player_status[i].card.hand_sub_card.append(GrainShovel)
            if sub_card_list[i * 3 + j] == 5:
                self.player_status[i].card.hand_sub_card.append(JunkWarehouse)
            if sub_card_list[i * 3 + j] == 6:
                self.player_status[i].card.hand_sub_card.append(LoamMiningSite)
            if sub_card_list[i * 3 + j] == 7:
                self.player_status[i].card.hand_sub_card.append(Manger)
            if sub_card_list[i * 3 + j] == 8:
                self.player_status[i].card.hand_sub_card.append(Pincer)
            if sub_card_list[i * 3 + j] == 9:
                self.player_status[i].card.hand_sub_card.append(Pitchfork)
            if sub_card_list[i * 3 + j] == 10:
                self.player_status[i].card.hand_sub_card.append(SilPan)
            if sub_card_list[i * 3 + j] == 11:
                self.player_status[i].card.hand_sub_card.append(WoolBlanket)
        self.player_status[i].card.start_sub_card = \
            deepcopy(self.player_status[i].card.hand_sub_card)

    job_card_list = random.sample(range(12), 12)
    for i in range(4):
        for j in range(3):
            if job_card_list[i * 3 + j] == 0:
                self.player_status[i].card.hand_job_card.append(Greengrocer)
            if job_card_list[i * 3 + j] == 1:
                self.player_status[i].card.hand_job_card.append(Hedger)
            if job_card_list[i * 3 + j] == 2:
                self.player_status[i].card.hand_job_card.append(KilnBaker)
            if job_card_list[i * 3 + j] == 3:
                self.player_status[i].card.hand_job_card.append(LivestockDealer)
            if job_card_list[i * 3 + j] == 4:
                self.player_status[i].card.hand_job_card.append(Lumberjack)
            if job_card_list[i * 3 + j] == 5:
                self.player_status[i].card.hand_job_card.append(Magician)
            if job_card_list[i * 3 + j] == 6:
                self.player_status[i].card.hand_job_card.append(Priest)
            if job_card_list[i * 3 + j] == 7:
                self.player_status[i].card.hand_job_card.append(Roofer)
            if job_card_list[i * 3 + j] == 8:
                self.player_status[i].card.hand_job_card.append(SkilledBrickLayer)
            if job_card_list[i * 3 + j] == 9:
                self.player_status[i].card.hand_job_card.append(SmallFarmer)
            if job_card_list[i * 3 + j] == 10:
                self.player_status[i].card.hand_job_card.append(SubCultivator)
            if job_card_list[i * 3 + j] == 11:
                self.player_status[i].card.hand_job_card.append(WarehouseManager)
        self.player_status[i].card.start_job_card = \
            deepcopy(self.player_status[i].card.hand_job_card)
        
def CONVERTER_to_VIRTUAL_FIELD(player_status):
    field = player_status.farm.field
    vfence = player_status.farm.vertical_fence
    hfence = player_status.farm.horizon_fence
    virtual_field = [[FieldType.NONE_FIELD for _ in range(11)] for _ in range(7)]
    #field mapping
    row_num = 0
    for row in field:
        col_num = 0
        for col in row:
            virtual_field[1+row_num*2][1+col_num*2] = col
            col_num += 1
        row_num += 1

    #vfence mapping
    row_num = 0
    for row in vfence:
        col_num = 0
        for col in row:
            # if col : virtual_field[row_num*2][1+col_num*2] = True
            # else: virtual_field[row_num*2][1+col_num*2] = False
            virtual_field[row_num*2][1+col_num*2] = col
            col_num += 1
        row_num += 1

    #hfence mapping
    row_num = 0
    for row in hfence:
        col_num = 0
        for col in row:
            # if col : virtual_field[1+row_num*2][col_num*2] = True
            # else: virtual_field[1+row_num*2][col_num*2] = False
            virtual_field[1+row_num*2][col_num*2] = col
            col_num += 1
        row_num += 1
    return virtual_field



from Agricola_Back.Agricola.behavior.unitbehavior.create_barn import CreateBarn


def ConstructFence(self,player):
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
                if self.horizontal_fence is True and self.player_status[player].farm.horizon_fence[i][j] is False:
                    cost += 1
        for i in range(3):
            for j in range(6):
                if self.vertical_fence is True and self.player_status[player].farm.vertical_fence[i][j] is False:
                    cost += 1
        if cost > self.player_status[player][
            self.game_status.now_turn_player].resource.wood:
            self.log_text = "나무가 모자랍니다."
            return False
        if not CreateCage(self.field_status, self.vertical_fence, self.horizontal_fence):
            self.log_text = "잘못된 동물 배치"
            return False
        self.player_status[player][
            self.game_status.now_turn_player].resource.wood -= cost
        self.log_text = "울타리 건설 성공"
        return True
    else:
        self.log_text = "울타리 건설 검증에 실패했습니다"
        return False
class FenceValidation():
    def __init__(self, field_status):
        self.field_status = copy(field_status)
        self.log_text = ""

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
                    if adjacent == 1:
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