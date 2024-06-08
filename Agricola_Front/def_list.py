import random
from copy import deepcopy
from collections import deque
from copy import copy

# from command import Command
# from Agricola.Agricola.entity.field_type import FieldType
from Agricola.Agricola.behavior.job.greengrocer import Greengrocer
from Agricola.Agricola.behavior.job.hedger import Hedger
from Agricola.Agricola.behavior.job.kiln_baker import KilnBaker
from Agricola.Agricola.behavior.job.livestock_dealer import LivestockDealer
from Agricola.Agricola.behavior.job.lumberjack import Lumberjack
from Agricola.Agricola.behavior.job.magician import Magician
from Agricola.Agricola.behavior.job.priest import Priest
from Agricola.Agricola.behavior.job.roofer import Roofer
from Agricola.Agricola.behavior.job.skilled_bricklayer import SkilledBrickLayer
from Agricola.Agricola.behavior.job.small_farmer import SmallFarmer
from Agricola.Agricola.behavior.job.sub_cultivator import SubCultivator
from Agricola.Agricola.behavior.job.warehouse_manager import WarehouseManager
from Agricola.Agricola.behavior.sub_facility.basket import Basket
from Agricola.Agricola.behavior.sub_facility.bottle import Bottle
from Agricola.Agricola.behavior.sub_facility.canoe import Canoe
from Agricola.Agricola.behavior.sub_facility.giant_farm import GiantFarm
from Agricola.Agricola.behavior.sub_facility.grain_shovel import GrainShovel
from Agricola.Agricola.behavior.sub_facility.junk_warehouse import JunkWarehouse
from Agricola.Agricola.behavior.sub_facility.loam_mining_site import LoamMiningSite
from Agricola.Agricola.behavior.sub_facility.manger import Manger
from Agricola.Agricola.behavior.sub_facility.pincer import Pincer
from Agricola.Agricola.behavior.sub_facility.pitchfork import Pitchfork
from Agricola.Agricola.behavior.sub_facility.silpan import SilPan
from Agricola.Agricola.behavior.sub_facility.wool_blanket import WoolBlanket
from Agricola.Agricola.behavior.basebehavior.construct_fence import ConstructFence
from Agricola.Agricola.entity.field_type import FieldType

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
    print(field)
    print(vfence)
    print(hfence)
    virtual_field = [[FieldType.NONE_FIELD for _ in range(11)] for _ in range(7)]
    #field mapping
    row_num = 0
    for row in field:
        col_num = 0
        for col in row:
            virtual_field[1+col_num*2][1+row_num*2] = col
            col_num += 1
        row_num += 1

    #vfence mapping
    row_num = 0
    for row in vfence:
        col_num = 0
        for col in row:
            # if col : virtual_field[row_num*2][1+col_num*2] = True
            # else: virtual_field[row_num*2][1+col_num*2] = False
            virtual_field[1+col_num*2][row_num*2] = col
            col_num += 1
        row_num += 1

    #hfence mapping
    row_num = 0
    for row in hfence:
        col_num = 0
        for col in row:
            # if col : virtual_field[1+row_num*2][col_num*2] = True
            # else: virtual_field[1+row_num*2][col_num*2] = False
            virtual_field[col_num*2][1+row_num*2] = col
            col_num += 1
        row_num += 1
    return virtual_field
from collections import deque


def animal_move_validation(field_status, animal_type, position):
    chk_already = check_already_placed(field_status, position)
    chk_same_type = check_same_type(field_status, animal_type, position)
    combined_status = chk_already[0] and chk_same_type[0]
    combined_log = [chk_already[1],chk_same_type[1]]
    return (combined_status, combined_log)


def check_already_placed(field_status, position):
    log_text = ""
    from Agricola.Agricola.entity.field_type import FieldType
    if field_status[position[0] * 2 + 1][position[1] * 2 + 1].field_type != FieldType.NONE_FIELD \
            and field_status[position[0] * 2 + 1][position[1] * 2 + 1].field_type != FieldType.CAGE:
        log_text = "다른 구조물 위에 동물을 놓을 수 없습니다."
        return (False, log_text)
    return (True, log_text)


def check_same_type(field_status, animal_type, position):
    check = [[0 for _ in range(11)] for _ in range(7)]
    queue = deque()
    log_text = ""
    from Agricola.Agricola.entity.animal_type import AnimalType
    from Agricola.Agricola.entity.farm.none_field import NoneField
    if field_status[position[0] * 2 + 1][position[1] * 2 + 1].kind != AnimalType.NONE \
            and field_status[position[0] * 2 + 1][position[1] * 2 + 1].kind != animal_type:
        log_text = "한 울타리 안에는 서로 다른 종류의 동물이 존재할 수 없습니다."
        return (False, log_text)

    if field_status[position[0] * 2 + 1][position[1] * 2 + 1].barn and isinstance(
            field_status[position[0] * 2 + 1][position[1] * 2 + 1], NoneField):
        return (True, log_text)
    check[position[0] * 2 + 1][position[1] * 2 + 1] = 1
    queue.append((position[0] * 2 + 1, position[1] * 2 + 1))
    while queue:
        x, y = queue.popleft()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for i in range(4):
            p = x + dx[i]
            q = y + dy[i]
            r = p + dx[i]
            s = q + dy[i]
            from Agricola.Agricola.entity.field_type import FieldType
            if 7 > r >= 0 and 0 <= s < 11 \
                    and check[r][s] == 0 and field_status[p][q].field_type != FieldType.FENCE \
                    and not (field_status[r][s].barn and isinstance(field_status[r][s], NoneField)):
                if field_status[r][s].kind != AnimalType.NONE \
                        and field_status[r][s].kind != animal_type:
                    log_text = "한 울타리 안에는 서로 다른 종류의 동물이 존재할 수 없습니다."
                    return (False, log_text)
                check[r][s] = 1
                queue.append((r, s))
    return (True, log_text)
