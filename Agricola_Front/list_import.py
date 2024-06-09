from qcr_converter import run_pyrcc5
# run_pyrcc5()#QRC 업데이트/
import sys,os,copy,random
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer,Qt
import data.MyQRC_rc as MyQRC_rc
from PyQt5.QtGui import QFont, QFontDatabase
from Agricola.Agricola.repository import player_status_repository,game_status_repository,round_status_repository,undo_repository
# from Agricola.Agricola.repository import P ,round_status_repository ,game_status_repository
from Agricola.Agricola.entity.field_type import FieldType
from Agricola.Agricola.entity.house_type import HouseType
from Agricola.Agricola.entity.crop_type import CropType
from Agricola.Agricola.entity.animal_type import AnimalType
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from Agricola.Agricola.gamestate.game_context import GameContext
from def_list import *

CARD_JOB_CONVERTER = {Greengrocer:0,Hedger:1,KilnBaker:2,LivestockDealer:3,Lumberjack:4,Magician:5,Priest:6,Roofer:7,SkilledBrickLayer:8,SmallFarmer:9,SubCultivator:10,WarehouseManager:11}
CARD_SUB_CONVERTER = {Basket:0,Bottle:1,Canoe:2,GiantFarm:3,GrainShovel:4,JunkWarehouse:5,LoamMiningSite:6,Manger:7,Pincer:8,Pitchfork:9,SilPan:10,WoolBlanket:11}

# from Agricola.Agricola.behavior.basebehavior import construct_barn, construct_fence,animal_move_validation,animal_position_validation
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
check_ui = uic.loadUiType(resource_path("data/check/check.ui"))[0] # worker 보드
text_log_ui = uic.loadUiType(resource_path("data/Basic/log.ui"))[0] # text log 박스
information_ui = uic.loadUiType(resource_path("data/Basic/information.ui"))[0] # information(설정, 점수표)
scoreboard_ui = uic.loadUiType(resource_path("data/Basic/scoreboard.ui"))[0] # 점수표
sidebar_ui = uic.loadUiType(resource_path("data/Basic/sidebar.ui"))[0] # 농장확대창 옆 사이드바
setting_ui = uic.loadUiType(resource_path("data/Basic/setting_pop.ui"))[0] # 세팅창
allcard_ui = uic.loadUiType(resource_path("data/Basic/allcard.ui"))[0] # 모든 카드
