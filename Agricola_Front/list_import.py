from qcr_converter import run_pyrcc5

import sys,os,copy,random
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer,Qt
import data.MyQRC_rc as MyQRC_rc
from PyQt5.QtGui import QFont, QFontDatabase
from Agricola_Back.Agricola.repository import player_status_repository,game_status_repository,round_status_repository,undo_repository
# from Agricola_Back.Agricola.repository import P ,round_status_repository ,game_status_repository
from Agricola_Back.Agricola.entity.field_type import FieldType
from Agricola_Back.Agricola.entity.house_type import HouseType
from Agricola_Back.Agricola.entity.crop_type import CropType
from Agricola_Back.Agricola.entity.animal_type import AnimalType
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from Agricola_Back.Agricola.gamestate.game_context import GameContext
from data.def_list import *
from Agricola_Back.Agricola.behavior.basebehavior.construct_barn import ConstructBarn
from Agricola_Back.Agricola.behavior.basebehavior.construct_fence import ConstructFence
from Agricola_Back.Agricola.entity.house_type import HouseType
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Agricola_Back/Agricola'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'))
from round_event import *
TYPE_Crop = ["GRAIN","VEGETABLE"]
CARD_JOB_CONVERTER = {Greengrocer:0,Hedger:1,KilnBaker:2,LivestockDealer:3,Lumberjack:4,Magician:5,Priest:6,Roofer:7,SkilledBrickLayer:8,SmallFarmer:9,SubCultivator:10,WarehouseManager:11}
CARD_SUB_CONVERTER = {Basket:0,Bottle:1,Canoe:2,GiantFarm:3,GrainShovel:4,JunkWarehouse:5,LoamMiningSite:6,Manger:7,Pincer:8,Pitchfork:9,SilPan:10,WoolBlanket:11}

# from Agricola_Back.Agricola.behavior.basebehavior import construct_barn, construct_fence,animal_move_validation,animal_position_validation
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
#UI파일 연결
main = uic.loadUiType(resource_path("data/mainwindow_v1.ui"))[0] # 진짜 메인
###개인 영역 UI들###
personal_field_ui = uic.loadUiType(resource_path("data/PersonalField/field_frame.ui"))[0] # 농장 15개 빈칸 뚫린 ui
field_base_ui = uic.loadUiType(resource_path("data/PersonalField/field_base.ui"))[0] # field 하나 ui
personal_resources_ui= uic.loadUiType(resource_path("data/PersonalField/personal_resource.ui"))[0] # 화면 전환되는 개인 자원
personal_card_ui= uic.loadUiType(resource_path("data/PersonalField/personal_card.ui"))[0] # 내가 낸 카드 ui
personal_card_small_ui = uic.loadUiType(resource_path("data/PersonalField/mycard_small.ui"))[0]
personal_card_big_ui = uic.loadUiType(resource_path("data/PersonalField/mycard_big.ui"))[0]
card_distribution_ui = uic.loadUiType(resource_path("data/Basic/mycard_firstcheck.ui"))[0] # 내가 낸 카드 ui
#personal_card_ui= uic.loadUiType(resource_path("PersonalField/mycards.ui"))[0] # 개인 카드 ui

###공동 영역 UI들###
log_viewer_ui= uic.loadUiType(resource_path("data/log_viewer_dialog.ui"))[0] # 로그
basic_roundcard_ui= uic.loadUiType(resource_path("data/Basic/roundcard.ui"))[0] # 라운드카드 ui
worker_board_ui = uic.loadUiType(resource_path("data/Basic/worker_board.ui"))[0] # worker 보드
check_ui = uic.loadUiType(resource_path("data/check/check_v2.ui"))[0] # worker 보드
text_log_ui = uic.loadUiType(resource_path("data/Basic/log.ui"))[0] # text log 박스
information_ui = uic.loadUiType(resource_path("data/Basic/information.ui"))[0] # information(설정, 점수표)
scoreboard_ui = uic.loadUiType(resource_path("data/Basic/scoreboard.ui"))[0] # 점수표
sidebar_ui = uic.loadUiType(resource_path("data/Basic/sidebar.ui"))[0] # 농장확대창 옆 사이드바
setting_ui = uic.loadUiType(resource_path("data/Basic/setting_pop.ui"))[0] # 세팅창
allcard_ui = uic.loadUiType(resource_path("data/Basic/allcard_v2.ui"))[0] # 모든 카드



def fence_validation(self):
   
    game_status = self.game_status
    player_status = self.player_status
    field_status = player_status[game_status.now_turn_player].farm.field
    vertical_fence = player_status[game_status.now_turn_player].farm.vertical_fence
    horizontal_fence = player_status[game_status.now_turn_player].farm.horizon_fence
    expanded_field = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]
    for i in range(3):
        for j in range(6):
            if vertical_fence[i][j] is True:
                expanded_field[i * 2 + 1][2 * j] = FieldType.FENCE
    for i in range(4):
        for j in range(5):
            if horizontal_fence[i][j] is True:
                expanded_field[i * 2][j * 2 + 1] = FieldType.FENCE
    for i in range(3):
        for j in range(5):
            expanded_field[i * 2 + 1][j * 2 + 1] = field_status[i][j].field_type
    field_status = expanded_field
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
    print(( check_fence_form() and check_connected_component_fence() and check_inside_object() and check_fence_count() ), log)
    return ( check_fence_form() and check_connected_component_fence() and check_inside_object() and check_fence_count() ), log
from Agricola_Back.Agricola.behavior.unitbehavior.create_cage import CreateCage
def asdfa(self):
        player_status = self.player_status
        game_status = self.game_status
        field_status = player_status[self.game_status.now_turn_player].farm.field
        vertical_fence = player_status[self.game_status.now_turn_player].farm.vertical_fence
        horizontal_fence = player_status[self.game_status.now_turn_player].farm.horizon_fence

        expanded_field = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]
        for i in range(3):
            for j in range(6):
                if vertical_fence[i][j] is True:
                    expanded_field[i * 2 + 1][2 * j] = FieldType.FENCE
        for i in range(4):
            for j in range(5):
                if horizontal_fence[i][j] is True:
                    expanded_field[i * 2][j * 2 + 1] = FieldType.FENCE
        for i in range(3):
            for j in range(5):
                expanded_field[i * 2 + 1][j * 2 + 1] = field_status[i][j].field_type
        fence_validation = FenceValidation(expanded_field)
        if fence_validation.execute():
            cost = 0
            for i in range(4):
                for j in range(5):
                    if horizontal_fence[i][j] is True and player_status[game_status.now_turn_player].farm.horizon_fence[i][j] is False:
                        cost += 1
            for i in range(3):
                for j in range(6):
                    if vertical_fence[i][j] is True and player_status[game_status.now_turn_player].farm.vertical_fence[i][j] is False:
                        cost += 1
            if cost > player_status[game_status.now_turn_player].resource.wood:
                log_text = "나무가 모자랍니다."
                return False,log_text
            if not CreateCage(field_status, vertical_fence, horizontal_fence):
                log_text = "잘못된 동물 배치"
                return False,log_text
            player_status[game_status.now_turn_player].resource.wood -= cost
            log_text = "울타리 건설 성공"
            return True,log_text
        else:
            log_text = "울타리 건설 검증에 실패했습니다"
            return False,log_text