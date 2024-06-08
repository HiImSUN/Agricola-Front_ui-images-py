import sys,os,copy,random
# 모듈이 위치한 디렉토리를 지정합니다.
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Agricola/Agricola'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'))
sys.dont_write_bytecode = True # pyc 생성 방지
from qcr_converter import run_pyrcc5
#run_pyrcc5()#QRC 업데이트/

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
personal_card_small_ui = uic.loadUiType(resource_path("data/PersonalField/mycard_small.ui"))[0] #mycard_small
personal_card_big_ui = uic.loadUiType(resource_path("data/PersonalField/mycard_big.ui"))[0] #mycard_big
card_distribution_ui = uic.loadUiType(resource_path("data/Basic/mycard_firstcheck.ui"))[0] # 내가 낸 카드 ui

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

# MAIN
class MainWindowClass(QMainWindow, main) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.init = True
# 폰트 파일 로드
        font_path = os.path.join(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'),'font'),'Pretendard-Medium.otf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family, 13)  # 로드된 폰트를 기본 폰트로 설정
        app.setFont(font)
        self.player_status = player_status_repository.PlayerStatusRepository().player_status
        self.game_status = game_status_repository.GameStatusRepository().game_status
        self.round_status = round_status_repository.RoundStatusRepository().round_status
        self.nowshow = 0
        #self.game_context = GameContext(self.game_status,self.player_status,self.round_status)
        from Agricola.Agricola.gameready import start_resource_distribution,round_card_shuffle
        print(StartResourceDistribution(self))  # 리소스 할당
        print(RoundCardShuffle(self))           # 라운드 카드 할당
        print(CardDistribution(self))           # 개인 카드 할당
        for i in range(4):
            self.player_status[i].card.start_job_card = deepcopy(self.player_status[i].card.hand_job_card)
            self.player_status[i].card.start_sub_card = deepcopy(self.player_status[i].card.hand_sub_card)
            self.player_status[i].card.put_job_card = deepcopy(self.player_status[i].card.hand_job_card)
            self.player_status[i].card.put_sub_card = deepcopy(self.player_status[i].card.hand_sub_card)
        

#플레이어 필드 위젯 설정
        self.personal_field = [WidgetPersonalField(i,self) for i in range(5)]
        for i in range(4):getattr(self,f"frm_p{i}_0").addWidget(self.personal_field[i])
#메인 필드 위젯 설정
        self.frm_main_field.addWidget(self.personal_field[4])
        for j in [1,3,5,7,9]:
            for lay in ["horizontalLayout_A","horizontalLayout_B","horizontalLayout_A_5",]:
                getattr(self.personal_field[4],lay).setStretch(j,6)
                                    # self.personal_field[4].verticalLayout_2.setStretch(j,1)
                                # self.personal_field[4].horizontalLayout_A.setStretch(10,2)
#플레이어 카드 위젯 설정
        self.personal_card = [PersonalCard_small(i,self) for i in range(4)]
        for i in range(4):getattr(self,f"frm_p{i}_1").addWidget(self.personal_card[i])
#메인 카드 위젯 설정
        self.main_card = [PersonalCard_big(self,player) for player in range(4)]
        for i in range(4):
            getattr(self,f"main_card__{i}").addWidget(self.main_card[i])
#사이드바 위젯 설정
        self.sidebar = SideBar(self)
        self.frm_main_sidebar.addWidget(self.sidebar)
        
#플레이어 리소스 위젯 설정
        self.personal_resource = [WidgetPersonalResource(i,self) for i in range(4)]
        for i in range(4):getattr(self,f"frm_p{i}_2").addWidget(self.personal_resource[i])
#베이직 라운드 위젯 설정
        self.basic_round = [WidgetBasicRound(i,self) for i in range(16)]
        [getattr(self,f"basic_{i}").addWidget(self.basic_round[i]) for i in range(16)]
# 랜덤위젯 설정
        numbers = list(range(14))
        random.shuffle(numbers)
        self.random_round = [WidgetrandomRound(i,numbers[i],self) for i in range(14)]
        [getattr(self,f"basic_{i+16}").addWidget(self.random_round[i]) for i in range(14)]
#워커보드 설정
        self.worker_board = WorkerBoard(self)
        self.vlo_etc_workerboard.addWidget(self.worker_board)
#인포메이션 칸(설정, 점수표)

        self.information = WidgetInformation(self)
        self.vlo_etc_information.addWidget(self.information)

        self.Class_check = Check(self)
        self.verticalLayout_37.addWidget(self.Class_check)
        ####################################init####################################
        self.timer_close,self.timer_open = QTimer(self),QTimer(self)
        self.log.clicked.connect(self.change_main_stacked)
        self.log.clicked.connect(self.update_state_of_all)
        self.pushButton_3.clicked.connect(self.round_test)
        self.log_popup = Log_viewer(self)
        self.media_player = QMediaPlayer()
        self.update_state_of_all()
        self.set_undo()
        ############################################################################
        self.stackedWidget.setCurrentIndex(2) # 게임시작 화면
        self.GAMESTART_BUTTON.clicked.connect(self.game_start)

        #카드 확인하면 다음사람에게 넘기기
        card_distribution = [FirstCardDistribution(self,i) for i in range(4)]
        for i in range(4):
            getattr(self,f'player_{i}_border').hide()
            getattr(self,f"sw_p{i}").setCurrentIndex(0) #확인 전 화면으로 설정해두고
            getattr(self,f"hlo_p{i}_card").addWidget(card_distribution[i]) #카드 분배 위젯 설정
            getattr(self, f"p{i}_show").clicked.connect(lambda _, x=i: getattr(myWindow, f"sw_p{x}").setCurrentIndex(1))
            getattr(self, f"p{i}_show").clicked.connect(lambda _, x=i: getattr(myWindow, f"card_check_p{x}").setEnabled(True))
            getattr(self, f"card_check_p{i}").clicked.connect(lambda _, x=i: self.stackedWidget.setCurrentIndex( (x+4)%7 ))
        self.card_check_p3.clicked.connect(self.open)
        self.verticalLayout.setStretch(0,0)
        self.verticalLayout.setStretch(2,0)






    def play_sound(self, sound_name):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),f'data/media/{sound_name}.mp3')  # 절대 경로로 변경
        print(f"Trying to play: {file_path}")
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return

        url = QUrl.fromLocalFile(file_path)
        self.media_player.setMedia(QMediaContent(url))
        if self.media_player.mediaStatus() == QMediaPlayer.NoMedia:
            print("Failed to load media.")
        else:
            print("Media loaded successfully.")
        
        self.media_player.play()
        print("Playing sound...")

    def open(self):
        self.verticalLayout.setStretch(0,1)
        self.verticalLayout.setStretch(2,1)
        for i in range(4):
            getattr(self,f'player_{i}_border').show()




    def game_start(self):

        pprint("게임이 시작되었습니다.")
        self.stackedWidget.setCurrentIndex(3) #player1의 카드 공개
        self.play_sound("bgm")

    def update_main_field(self, player):
        field = player_status_repository.player_status_repository.player_status[5].farm.field = deepcopy(player_status_repository.player_status_repository.player_status[player].farm.field)
        horizon_fence = player_status_repository.player_status_repository.player_status[5].farm.horizon_fence = deepcopy(player_status_repository.player_status_repository.player_status[player].farm.horizon_fence)
        vertical_fence = player_status_repository.player_status_repository.player_status[5].farm.vertical_fence = deepcopy(player_status_repository.player_status_repository.player_status[player].farm.vertical_fence)        
        for _ in range(15):
            i = _ // 5
            j = _ % 5
            myWindow.personal_field[4].field[_].update_state_want_field(field[i][j])
        for i, row in enumerate(horizon_fence):
            for j, fence in enumerate(row):
                getattr(myWindow.personal_field[4], f"btn_fence_h{i}{j}").setEnabled(False)
                if fence:
                    getattr(myWindow.personal_field[4], f"btn_fence_h{i}{j}").setStyleSheet(f"border-image: url(:/newPrefix/images/fence_h_{self.parent.game_status.now_turn_player};")
                else:
                    getattr(myWindow.personal_field[4], f"btn_fence_h{i}{j}").setStyleSheet("border-image:none;")
        for i, row in enumerate(vertical_fence):
            for j, fence in enumerate(row):
                getattr(myWindow.personal_field[4], f"btn_fence_v{i}{j}").setEnabled(False)
                if fence:
                    getattr(myWindow.personal_field[4], f"btn_fence_v{i}{j}").setStyleSheet(f"border-image: url(:/newPrefix/images/fence_v_{self.parent.game_status.now_turn_player};")
                else:
                    getattr(myWindow.personal_field[4], f"btn_fence_v{i}{j}").setStyleSheet("border-image:none;")

        
    def round_test(self):
        self.game_status.now_round = (self.game_status.now_round+1)%15
        pprint(f"현재 라운드는 {self.game_status.now_round}라운드입니다.")
        self.update_state_of_all()
        [getattr(self,f"basic_{i+16}").addWidget(self.random_round[i]) for i in range(13)]

    def set_undo(self):
        self.undo_player = deepcopy(self.player_status)
        hand_undo_gameStatus = deepcopy(self.game_status)
        self.undo_round = deepcopy(self.round_status)
        
    def undo(self):
        self.player_status = self.undo_player
        self.game_status = self.undo_gameStatus
        self.round_status = self.undo_round
        self.set_undo()
        self.update_state_of_all()
        pprint("턴 초기 화면으로 돌아갔습니다.")

    def pprint(self,text):
        print(text)
        self.log_2.setText(self.log_2.toPlainText()+"\n"+str(text))
        scroll_bar = self.log_2.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())
        self.log_popup.logging(text)

    # def change_main_stacked(self):
    #     self.update_state_of_all()
    #     currentWidget = self.stackedWidget.currentWidget().objectName()
    #     # if index == 0:self.stackedWidget.setCurrentIndex(1)
    #     # else:self.stackedWidget.setCurrentIndex(0)
    #     if currentWidget == "round_page":self.change_stacked_page("personal_page")
    #     else:self.change_stacked_page("round_page")
    def change_main_stacked(self, player):
        self.update_main_field(player)
        current = myWindow.stackedWidget.currentIndex()
        if current == 0: #라운드 화면이면
            #값 업데이트 해주고
            myWindow.stackedWidget.setCurrentIndex(1)
        elif current == 1:
            myWindow.stackedWidget.setCurrentIndex(0)
        else:
            pprint("현재 페이지에선 창전환을 할 수 없습니다.")


    def change_stacked_page(self, after_page):
        after_page = getattr(self, after_page)
        stacked_Widget = self.stackedWidget
        if not self.timer_close.isActive() and not self.timer_open.isActive():
            # 이걸로 속도 조절 낮을수록 빠름
            self.speed = 5
            self.timer_close = QTimer(self)
            self.timer_open = QTimer(self)
            self.total_timer_count = 10
            self.current_timer_count = 0
            self.timer_open.stop()
            self.timer_close.stop()
            self.timer_close.timeout.connect(lambda : process_timer_close(self,after_page))
            self.timer_close.start(self.speed)
            self.timer_open.timeout.connect(lambda : process_timer_open(self,after_page))
        def process_timer_close(self,after_page):
            self.opacity_effect = QGraphicsOpacityEffect(stacked_Widget.currentWidget())
            self.opacity_effect_after = QGraphicsOpacityEffect(after_page)
            self.opacity_effect_after.setOpacity(0)
            self.opacity_effect.setOpacity(1-0.1*self.current_timer_count)
            stacked_Widget.currentWidget().setGraphicsEffect(self.opacity_effect)
            self.current_timer_count += 1
            if self.current_timer_count == self.total_timer_count:
                stacked_Widget.setCurrentWidget(after_page)
                while not after_page.isVisible():
                    pass
                # self.title.setText(title)
                self.timer_open.start(self.speed)
                self.timer_close.stop()
                self.opacity_effect_after.setOpacity(1)
        def process_timer_open(self,after_page):
            self.opacity_effect_after.setOpacity(1-0.1*self.current_timer_count)
            after_page.setGraphicsEffect(self.opacity_effect_after)
            self.current_timer_count -= 1
            if self.current_timer_count == 0:
                self.timer_open.stop()
    def update_state(self):
        # for i in range(4):
        #     getattr(self,f"player_{i}_border").setStyleSheet("")
        i = self.game_status.now_turn_player
        # getattr(self,f"player_{i}_border").setStyleSheet(f"#player_{i}_border{{border:3px solid blue;}}")
        self.stcked_main_card.setCurrentWidget(getattr(self,f"main_card_{i}"))

    def update_state_of_all(self):
# resource 업데이트
# field 업데이트
        for c in self.personal_field:
            c.update_state()
            for cc in c.field: cc.update_state()
        # for c in self.personal_card:
        #     c.update_state()
        for c in self.personal_resource:
            c.update_state()
        for widget in self.random_round:
            widget.update_state()
#메인 플레이어 보더 업데이트
        for widget in self.personal_card:
            widget.update_state()
        for widget in self.main_card:
            widget.update_state()

        # self.main_card.update_state()
        self.worker_board.update_state()
        self.update_state()

















class WidgetPersonalField(QWidget, personal_field_ui) :
    def __init__(self, player,parent) :
        super().__init__()
        self.setupUi(self)
        self.player = player
        self.parent = parent
        self.field = [WidgetFieldBase(i,self) for i in range(15) ]# field_0 ~ field_14 까지
        self.state = 0
        
        tmp_field_num = 0
        for i in range(3):
            for j in range(5):
                field = self.field[tmp_field_num]
                layout = getattr(self, f'hlo_{i}_{j}')
                layout.addWidget(field)
                tmp_field_num += 1

        # fence 객체들에 대하여 버튼 클릭 이벤트 추가
        if self.player == 4:
            for j in range(4):
                for i in range(5):
                    getattr(self, f'btn_fence_h{j}{i}').clicked.connect(lambda _, v="h",i=i,j=j: self.press_fence(v,j,i))
            for j in range(3):
                for i in range(6):
                    getattr(self, f'btn_fence_v{j}{i}').clicked.connect(lambda _,v="v", i=i,j=j: self.press_fence(v,j,i))
        else :
            for j in range(4):
                for i in range(5):
                    getattr(self, f'btn_fence_h{j}{i}').clicked.connect(self.parent.change_main_stacked) #TODO
                    getattr(self, f'btn_fence_h{j}{i}').setCheckable(False)
            for j in range(3):
                for i in range(6):
                    getattr(self, f'btn_fence_v{j}{i}').clicked.connect(self.parent.change_main_stacked) #TODO
                    getattr(self, f'btn_fence_v{j}{i}').setCheckable(False)

    def mousePressEvent(self,event):
        pprint(f"Pressed personalField Player ID : {self.player}")
        if self.state == 0:
            if self.player != 4:
                if myWindow.stackedWidget.currentIndex() == 0: #라운드 화면이면
                    self.parent.change_main_stacked() #창 바꿔주고
                elif myWindow.stackedWidget.currentIndex() == 1: #이미 농장 칸이면
                    if myWindow.nowshow == self.player: #그리고 그 농장이 본인의 농장이면
                        print("#그리고 그 농장이 본인의 농장이면")
                        self.parent.change_main_stacked() #창 바꿔주고
                    else: #본인의 농장이 아니라면 본인의 농장으로 화면 업데이트
                        print("본인의 농장이 아니라면 본인의 농장으로 화면 업데이트")
                        myWindow.nowshow = self.player
                        #확대 농장을 player걸로 업데이트
                        pass
                    
                
            

    def changeDefaultMode(self): # 창을 전환만 해야 한다.
        self.state = 0

    def changeSetFenceMode(self):
        self.state = 1

    def press_fence(self, v,j,i):
        # try:
        player = myWindow.game_status.now_turn_player
        if v == "v":
            self.parent.player_status[player].farm.vertical_fence[j][i] = not self.parent.player_status[player].farm.vertical_fence[j][i]
        else:
            self.parent.player_status[player].farm.horizon_fence[j][i] = not self.parent.player_status[player].farm.horizon_fence[j][i]

            # self.parent.player_status[self.player].farm.horizon_fence[j][i] = not self.parent.player_status[self.player].farm.horizon_fence[j][i]
        # pprint(f"{v}{j}{i}펜스 설치")
        # except:
            # pprint("오류오류")
        # pprint(f"Player ID : {self.player} | Fence ID: {v}{j}{i}")
        update()

    def update_state(self):
        # 턴 비활성화
        if self.player == 4:
            now_player = self.parent.game_status.now_turn_player
        else:
            player = self.player
        #self.setEnabled(self.player == self.parent.game_status.now_turn_player)
        
        #펜스 state
        # for j in range(4):
        #     for i in range(5):
        #         if self.parent.player_status[player].farm.horizon_fence[j][i] == True:
        #             getattr(self, f'btn_fence_h{j}{i}').setStyleSheet(f"border:0.5px solid rgba(255, 255, 255, 128);border-image : url(:/newPrefix/images/fence_h_{player}.png);")
        #         else:
        #             getattr(self, f'btn_fence_h{j}{i}').setStyleSheet("border:0.5px solid rgba(255, 255, 255, 128);border-image : none;")
        # for j in range(3):
        #     for i in range(6):
        #         if self.parent.player_status[player].farm.vertical_fence[j][i] == True:
        #             getattr(self, f'btn_fence_v{j}{i}').setStyleSheet(f"border:0.5px solid rgba(255, 255, 255, 128);border-image : url(:/newPrefix/images/fence_v_{player}.png);")
        #         else:
        #             getattr(self, f'btn_fence_v{j}{i}').setStyleSheet("border:0.5px solid rgba(255, 255, 255, 128);border-image : none;")

class WidgetFieldBase(QWidget, field_base_ui) :
    def __init__(self, id,parent):
        super().__init__()
        self.setupUi(self)
        self.id = id # field에게 고유 id (0~14) 부여
        self.i = self.id//5
        self.j = self.id%5
        self.parent = parent
        self.player = self.parent.player #어떤 플레이어의 땅인지
        self.lb_unit.setStyleSheet("border:none;")
        self.lb_barn.setStyleSheet("border:none;")
        self.count.setText("")
        self.state = 0 # 0:창전환용 1:경작지 2:동물옮기기 3:식물심기
        if self.player == 4: pass
            #self.lb_unit.clicked.connect(self.change_unit) #########################################
            #self.lb_barn.clicked.connect(self.change_barn) #########################################
        else: pass
            #self.lb_unit.clicked.connect(self.parent.parent.change_main_stacked)
            #self.lb_barn.clicked.connect(self.parent.parent.change_main_stacked)

    def changeArableMode(self):
        self.state = 1
    def changeSetUnitMode(self):
        self.state = 2
    def changeBarnMode(self):
        self.state = 3
    #################################$%^$%^$%^
    def mousePressEvent(self,event):
        print(event)
        print('hi')
        if self.state == 0:
            if myWindow.stackedWidget.currentIndex() == 0: #라운드 화면이면
                myWindow.change_main_stacked()
            elif myWindow.stackedWidget.currentIndex() == 1: #농장화면인데
                if self.player == myWindow.nowshow :
                    myWindow.change_main_stacked()
                else:
                    myWindow.nowshow = self.player
                    #self.player에 맞게 화면 재구성


        if self.state == 1: #Arable
            from Agricola.Agricola.entity.farm.none_field import NoneField
            from Agricola.Agricola.entity.farm.arable_land import ArableLand
            if isinstance(player_status_repository.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player].farm.field[self.i][self.j], NoneField):
                print("step1")
                if isinstance(player_status_repository.player_status_repository.player_status[5].farm.field[self.i][self.j], NoneField):
                    print("step2")
                    myWindow.personal_field[4].Form.setSyleSheet("border-image: url(:/newPrefix/images/arable_land.png);")
                    player_status_repository.player_status_repository.player_status[4].farm.field[self.i][self.j] = ArableLand()
                else :
                    print("step3")
                    myWindow.personal_field[4].Form.setSyleSheet("border-image: url(:/newPrefix/images/empty_field.png);")
                    player_status_repository.player_status_repository.player_status[4].farm.field[self.i][self.j] = NoneField()
        if self.state == 2:
            pass
        if self.state == 3:
            pass

    # def mousePressEvent(self,event):
    #     if self.player != 4:
    #         self.parent.parent.change_main_stacked()
    #     else:
    #         pprint(f"Pressed Fance Player ID : {self.parent.player} |  ID: {self.id}")
    #         self.change_house ()
    #         myWindow.player_status[myWindow.game_status.now_turn_player].farm.field[self.i][self.j].count+=1
    #         myWindow.update_state_of_all()

    def change_barn(self):
        player = myWindow.game_status.now_turn_player
        pprint(f"Player ID : {player} | Fence ID: {self.id} | Type: barn")

        myWindow.player_status[player].farm.field[self.i][self.j].barn = not myWindow.player_status[player].farm.field[self.i][self.j].barn
        myWindow.update_state_of_all()
        pprint("외양간 변경")
    def change_house(self):
        player = myWindow.game_status.now_turn_player
        # print("player : "+str(player))
        rand = [HouseType.DIRT,HouseType.STONE,HouseType.WOOD]
        rand.remove(getattr(HouseType,myWindow.player_status[player].farm.house_status.name))
        random.shuffle(rand)
        # print(rand)
        myWindow.player_status[player].farm.house_status = rand[0]
        myWindow.update_state_of_all()
    def change_unit(self):
        pprint("change_unit")
        player = myWindow.game_status.now_turn_player
        # print("player : "+str(player))
        selected_animal = getattr(AnimalType,self.parent.parent.sidebar.checked.split('_')[-1].upper())
        print(animal_move_validation(CONVERTER_to_VIRTUAL_FIELD(myWindow.player_status[player]),selected_animal,(self.i,self.j)))
        rand = [AnimalType.NONE,AnimalType.COW,AnimalType.PIG,AnimalType.SHEEP]#,CropType.GRAIN,CropType.NONE,CropType.VEGETABLE]
        # print(myWindow.player_status[player].farm.field[self.i][self.j].kind)
        # try:
        #     rand.remove(getattr(AnimalType,myWindow.player_status[player].farm.field[self.i][self.j].kind.name))
        # except:
        #     try:
        #         rand.remove(getattr(CropType,myWindow.player_status[player].farm.field[self.i][self.j].kind.name))
        #     except:
        #         rand = [CropType.GRAIN,CropType.NONE,CropType.VEGETABLE]

        # random.shuffle(rand)
        # animal = rand[0]
        # # print(rand)
        # print(animal)
        # print(animal, (self.i,self.j))
        # self.vertical_fence=myWindow.player_status[player].farm.vertical_fence
        # self.horizontal_fence=myWindow.player_status[player].farm.horizon_fence
        # myWindow.player_status[player].farm.field[self.i][self.j].kind = rand[0]

        if True:
            if self.parent.parent.sidebar.checked!="":
                print( myWindow.player_status[player].farm.field[self.i][self.j].kind)
                print(selected_animal)
                print( myWindow.player_status[player].farm.field[self.i][self.j].kind==selected_animal)
                print( myWindow.player_status[player].farm.field[self.i][self.j].kind.value==('NONE'))
                if myWindow.player_status[player].farm.field[self.i][self.j].kind == selected_animal or myWindow.player_status[player].farm.field[self.i][self.j].kind.value==0:    
                    myWindow.player_status[player].farm.field[self.i][self.j].kind = selected_animal
                    myWindow.player_status[myWindow.game_status.now_turn_player].farm.field[self.i][self.j].count+=1
                else: pprint("다른 종류의 동물이 올라갈 수 없습니다.")
            else: 
                if myWindow.player_status[myWindow.game_status.now_turn_player].farm.field[self.i][self.j].count>0:
                    myWindow.player_status[myWindow.game_status.now_turn_player].farm.field[self.i][self.j].count-=1
                if myWindow.player_status[myWindow.game_status.now_turn_player].farm.field[self.i][self.j].count==0:
                    myWindow.player_status[myWindow.game_status.now_turn_player].farm.field[self.i][self.j].kind = AnimalType.NONE


        #myWindow.update_state_of_all()

    def update_state(self):
        if self.player == 4:
            player = self.parent.parent.game_status.now_turn_player
        else:
            player = self.player

        CONVERTER_image={(0,0):"empty_field",(0,1):"empty_field",(0,2):"empty_field",(0,3):"empty_field",(1,0):"arable_land",(1,1):"arable_land",(1,2):"arable_land",(1,3):"arable_land",(2,0):"empty_field",(2,1):"empty_field",(2,2):"empty_field",(2,3):"empty_field",(3,1):"house_dirt",(3,2):"house_wood",(3,3):"house_stone"}
        
        # for player in range(4):
        house_status = self.parent.parent.player_status[player].farm.house_status.value # 집 종류 파악
        # print(house_status)

        # 배경화면 바꾸기
        field_status = self.parent.parent.player_status[player].farm.field[self.i][self.j].field_type.value
        self.widget.setStyleSheet(f"#widget{{border-image : url(:/newPrefix/images/{CONVERTER_image[field_status,house_status]}.png);}}")
        # 유닛 처리
        unit = self.parent.parent.player_status[player].farm.field[self.i][self.j].kind
        if not unit==None:
            kind = self.parent.parent.player_status[player].farm.field[self.i][self.j].kind.name.lower()
            if not kind == "none":
                self.lb_unit.setStyleSheet(f"#lb_unit{{border-image : url(:/newPrefix/images/{self.parent.parent.player_status[player].farm.field[self.i][self.j].kind.name.lower()}.png);}}")
            else:
                self.lb_unit.setStyleSheet(f"#lb_unit{{border:none;}}")
        else:
            self.lb_unit.setStyleSheet(f"#lb_unit{{border:none;}}")
        count = self.parent.parent.player_status[player].farm.field[self.i][self.j].count if self.parent.parent.player_status[player].farm.field[self.i][self.j].count not in [0,None] else ""
        self.count.setText(str(count))
        # 외양간 처리
        if self.parent.parent.player_status[player].farm.field[self.i][self.j].barn:
            styleSheet = f"QPushButton#lb_barn {{border-image: url(:/newPrefix/images/barn_{player}.png);}}"
        else:
            styleSheet = f"QPushButton#lb_barn {{border: none;}}"
        self.lb_barn.setStyleSheet(styleSheet)
        pass

    def update_state_want_field(self, field):
        if self.player == 4:
            player = self.parent.parent.game_status.now_turn_player
        else:
            player = self.player

        CONVERTER_image={(0,0):"empty_field",(0,1):"empty_field",(0,2):"empty_field",(0,3):"empty_field",(1,0):"arable_land",(1,1):"arable_land",(1,2):"arable_land",(1,3):"arable_land",(2,0):"empty_field",(2,1):"empty_field",(2,2):"empty_field",(2,3):"empty_field",(3,1):"house_dirt",(3,2):"house_wood",(3,3):"house_stone"}
        
        # for player in range(4):
        house_status = self.parent.parent.player_status[player].farm.house_status.value # 집 종류 파악
        # print(house_status)

        # 배경화면 바꾸기
        field_status = field.field_type.value
        self.widget.setStyleSheet(f"#widget{{border-image : url(:/newPrefix/images/{CONVERTER_image[field_status,house_status]}.png);}}")
        # 유닛 처리
        unit = field.kind
        if not unit==None:
            kind = field.kind.name.lower()
            if not kind == "none":
                self.lb_unit.setStyleSheet(f"#lb_unit{{border-image : url(:/newPrefix/images/{field.kind.name.lower()}.png);}}")
            else:
                self.lb_unit.setStyleSheet(f"#lb_unit{{border:none;}}")
        else:
            self.lb_unit.setStyleSheet(f"#lb_unit{{border:none;}}")
        count = field.count if field.count not in [0,None] else ""
        self.count.setText(str(count))
        # 외양간 처리
        if field.barn:
            styleSheet = f"QPushButton#lb_barn {{border-image: url(:/newPrefix/images/barn_{player}.png);}}"
        else:
            styleSheet = f"QPushButton#lb_barn {{border: none;}}"
        self.lb_barn.setStyleSheet(styleSheet)

        
# 개인 농장 오른 쪽 아이콘으로 보이는 작은 카드창
class PersonalCard_small(QWidget, personal_card_small_ui):
    def __init__(self, player, parent):
        super().__init__()
        self.setupUi(self)
        self.player = player
        self.parent = parent
        list_sub = [CARD_SUB_CONVERTER[c] for c in self.parent.player_status[player].card.start_sub_card]
        list_job = [CARD_JOB_CONVERTER[c] for c in self.parent.player_status[player].card.start_job_card]
        
        for i in range(3):
            getattr(self,f"widget_sub_{i+1}").setStyleSheet(f"#widget_sub_{i+1}{{border-image: url(:/newPrefix/images/보조 설비/보조설비{list_sub[i]}.png);}}#widget_sub_{i+1}:disabled{{border-image: url(:/newPrefix/images/보조 설비/보조설비back.png);}}")
            getattr(self,f"widget_job_{i+1}").setStyleSheet(f"#widget_job_{i+1}{{border-image: url(:/newPrefix/images/직업 카드/직업카드{list_job[i]}.png);}}#widget_job_{i+1}:disabled{{border-image: url(:/newPrefix/images/직업 카드/직업카드back.png);}}")
            print(f"#widget_job_{i+1}{{border-image: url(:/newPrefix/images/직업 카드/직업카드{list_job[i]}.png);}}#widget_sub_{i+1}:disabled{{border-image: url(:/newPrefix/images/직업 카드/직업카드back.png);}}")
            getattr(self,f"widget_main_{i+1}").setStyleSheet(f"#widget_main_{i+1}{{border-image: url(:/newPrefix/images/주요 설비/주요설비아이콘.png);}}#widget_job_{i+1}:disabled{{border:none;}}")
        
        # self.setEnabled(False)
        
        self.update_state()
    def mousePressEvent(self, event):
        self.setEnabled(self.player == self.parent.game_status.now_turn_player)
        pprint(f"Pressed personalField Player ID : {self.player}")
        self.parent.change_main_stacked()  
    def update_state(self):
        # player = self.parent.game_status.now_turn_player
        player = self.player
        list_sub = [CARD_SUB_CONVERTER[c] for c in self.parent.player_status[player].card.start_sub_card]
        list_job = [CARD_JOB_CONVERTER[c] for c in self.parent.player_status[player].card.start_job_card]
        list_put_sub = [CARD_SUB_CONVERTER[c] for c in self.parent.player_status[player].card.put_sub_card]
        list_put_job = [CARD_JOB_CONVERTER[c] for c in self.parent.player_status[player].card.put_job_card]
        list_put_main = self.parent.player_status[player].card.put_main_card
        print(list_job,list_put_job,list_job[0] not in list_put_job)
        for i in range(3):
            getattr(self,f"widget_sub_{i+1}").setEnabled(list_sub[i] in list_put_sub)
            getattr(self,f"widget_job_{i+1}").setEnabled(list_job[i] in list_put_job)

        # for i in range(5):
        #     if i<len(list_put_job):
        #         getattr(self,f"widget_main_{i+1}").setStyleSheet(f"border-image: url(:/newPrefix/images/주요 설비/주요설비{list_put_job[i]}.png);")
        #     else:
        #         # getattr(self,f"widget_main_{i+1}").setStyleSheet(f"border:none;")
        #         getattr(self,f"widget_main_{i+1}").hide()
# 메인 창에 뜰 개인별 카드 창
class PersonalCard_big(QWidget, personal_card_big_ui):
    def __init__(self, parent,player):
        super().__init__()
        self.setupUi(self)
        self.player = player
        self.parent = parent
        list_sub = [CARD_SUB_CONVERTER[c] for c in self.parent.player_status[player].card.start_sub_card]
        list_job = [CARD_JOB_CONVERTER[c] for c in self.parent.player_status[player].card.start_job_card]
        
        for i in range(3):
            getattr(self,f"widget_sub_{i+1}").setStyleSheet(f"#widget_sub_{i+1}{{border-image: url(:/newPrefix/images/보조 설비/보조설비{list_sub[i]}.png);}}#widget_sub_{i+1}:disabled{{border-image: url(:/newPrefix/images/보조 설비/보조설비back.png);}}")
            getattr(self,f"widget_job_{i+1}").setStyleSheet(f"#widget_job_{i+1}{{border-image: url(:/newPrefix/images/직업 카드/직업카드{list_job[i]}.png);}}#widget_job_{i+1}:disabled{{border-image: url(:/newPrefix/images/직업 카드/직업카드back.png);}}")
            
            print(f"#widget_job_{i+1}{{border-image: url(:/newPrefix/images/직업 카드/직업카드{list_job[i]}.png);}}#widget_sub_{i+1}:disabled{{border-image: url(:/newPrefix/images/직업 카드/직업카드back.png);}}")
    def mousePressEvent(self, event):
        player = self.parent.game_status.now_turn_player
        pprint(f"Pressed personalField Player ID : {player}")
    def update_state(self):
        player = self.parent.game_status.now_turn_player

        player = self.player
        list_sub = [CARD_SUB_CONVERTER[c] for c in self.parent.player_status[player].card.start_sub_card]
        list_job = [CARD_JOB_CONVERTER[c] for c in self.parent.player_status[player].card.start_job_card]
        list_put_sub = [CARD_SUB_CONVERTER[c] for c in self.parent.player_status[player].card.put_sub_card]
        list_put_job = [CARD_JOB_CONVERTER[c] for c in self.parent.player_status[player].card.put_job_card]
        list_put_main = self.parent.player_status[player].card.put_main_card
        print(list_job,list_put_job,list_job[0] not in list_put_job)
        for i in range(3):
            getattr(self,f"widget_sub_{i+1}").setEnabled(list_sub[i] in list_put_sub)
            getattr(self,f"widget_job_{i+1}").setEnabled(list_job[i] in list_put_job)
            getattr(self,f"label_sub_{i+1}").setText(str(list_sub[i]) if list_sub[i] in list_put_sub else "")
            getattr(self,f"label_job_{i+1}").setText(str(list_job[i]) if list_job[i] in list_put_job else "")
class WidgetPersonalResource(QWidget, personal_resources_ui) :
    def __init__(self, player,parent) :
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.setupUi(self)
        self.player = player
        self.parent = parent
        self.turn_info_1.setText("")
        self.turn_info_2.setText("")
    def mousePressEvent(self,event):
        pprint(f"Pressed Resource Player ID : {self.player}")
        index = self.stackedWidget.currentIndex()
        if index == 0:self.stackedWidget.setCurrentIndex(1)
        else:self.stackedWidget.setCurrentIndex(0)
    def update_state(self):
        # for player in range(4):
        player = self.player 

        for t in ["dirt","grain","reed","stone","vegetable","wood",'beg_token',"food"]:
            getattr(self,f"count_{t}").setText(str(getattr(self.parent.player_status[player].resource,t)))
        for t in ['sheep','cow','pig','barn','fence']:
            getattr(self,f"count_{t}").setText(str(getattr(self.parent.player_status[player].farm,f"get_{t}_count")()))

        #     # self.personal_resource[player].count_dirt.setText(str(self.player.player_status[player].resource.dirt))
        #     getattr(self,f"count_{t}").setText(str(getattr(self.parent.player_status[player].farm,t)))
            
        getattr(self,f"count_worker").setText(str(self.parent.player_status[player].worker+self.parent.player_status[player].baby))
        "Fence 는 아직 진행중"
        # for t in ["fence",]:
        #     # getattr(self.personal_resource[player],f"count_{t}").setText(str(getattr(self.player_status[player].resource,t)))
        #     getattr(self.personal_resource[player],f"count_{t}")

        if self.parent.game_status.now_turn_player == player:
            self.turn_info_1.setText("NOW")
            self.turn_info_2.setText("NOW")
        elif self.parent.game_status.next_turn_player ==player:
            self.turn_info_1.setText("NEXT")
            self.turn_info_2.setText("NEXT")
        else :
            self.turn_info_1.setText("")
            self.turn_info_2.setText("")
        if self.parent.player_status[self.player].resource.first_turn:
            self.lb_turn_icon_1.show()
            self.lb_turn_icon_2.show()
        else:
            self.lb_turn_icon_1.hide()
            self.lb_turn_icon_2.hide()
            
class WidgetBasicRound(QWidget, basic_roundcard_ui) :
    def __init__(self,num,parent) :
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.parent = parent
        self.num = num
        self.setupUi(self)
        self.btn_round_1.setText('')
        self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/기본행동/기본행동 ({self.num}).png);}}")
        self.btn_round_4.hide()
        # for i in range(5):
        #     getattr(self,f"btn_round_{i}").clicked.connect(self.roundClick)

    def mousePressEvent(self,event):
        from Agricola.Agricola.entity.card_factory import basic_card_command_factory
        from Agricola.Agricola.behavior.can_enter_base_behavior import CanEnterBaseBehavior
        can = CanEnterBaseBehavior(self.num)
        if can.execute():
            act = basic_card_command_factory(self.num)
            print(act)
            playlist = act().execute()
            print(playlist)
            from Agricola.Agricola.behavior.basebehavior.arable_expansion import ArableExpansion
            from Agricola.Agricola.behavior.basebehavior.house_expansion import HouseExpansion
            from Agricola.Agricola.behavior.basebehavior.construct_barn import ConstructBarn
            from Agricola.Agricola.behavior.unitbehavior.playable_sub_facility_listup import PlayableSubCardListup
            from Agricola.Agricola.behavior.basebehavior.buy_sub_card import BuySubCard
            from Agricola.Agricola.behavior.unitbehavior.playable_sub_job_listup import PlayableJobCardListup
            from Agricola.Agricola.behavior.basebehavior.buy_job_card_1 import BuyJobCard1
            from Agricola.Agricola.behavior.basebehavior.buy_job_card_2 import BuyJobCard2
            from Agricola.Agricola.behavior.unitbehavior.use_worker import UseWorker
            #############################!@#!@#@!#!@#!@#!@#!!@#!@#!@#!@#
            for play in playlist:
                if play.__name__ == "ArableExpansion":
                    field = player_status_repository.player_status_repository.player_status[5].farm.field = deepcopy(player_status_repository.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player].farm.field)
                    horizon_fence = player_status_repository.player_status_repository.player_status[5].farm.horizon_fence = deepcopy(player_status_repository.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player].farm.horizon_fence)
                    vertical_fence = player_status_repository.player_status_repository.player_status[5].farm.vertical_fence = deepcopy(player_status_repository.player_status_repository.player_status[game_status_repository.game_status_repository.game_status.now_turn_player].farm.vertical_fence)        
                    for _ in range(15):
                        i = _ // 5
                        j = _ % 5
                        myWindow.personal_field[4].field[_].changeArableMode()
                        myWindow.personal_field[4].field[_].update_state_want_field(field[i][j])
                    for i, row in enumerate(horizon_fence):
                        for j, fence in enumerate(row):
                            getattr(myWindow.personal_field[4], f"btn_fence_h{i}{j}").setEnabled(False)
                            if fence:
                                getattr(myWindow.personal_field[4], f"btn_fence_h{i}{j}").setStyleSheet(f"border-image: url(:/newPrefix/images/fence_h_{self.parent.game_status.now_turn_player};")
                            else:
                                getattr(myWindow.personal_field[4], f"btn_fence_h{i}{j}").setStyleSheet("border-image:none;")
                    for i, row in enumerate(vertical_fence):
                        for j, fence in enumerate(row):
                            getattr(myWindow.personal_field[4], f"btn_fence_v{i}{j}").setEnabled(False)
                            if fence:
                                getattr(myWindow.personal_field[4], f"btn_fence_v{i}{j}").setStyleSheet(f"border-image: url(:/newPrefix/images/fence_v_{self.parent.game_status.now_turn_player};")
                            else:
                                getattr(myWindow.personal_field[4], f"btn_fence_v{i}{j}").setStyleSheet("border-image:none;")
                    myWindow.stackedWidget.setCurrentIndex(1) # 개인 창으로 전환하기
                    for player in range(4):
                        myWindow.personal_field[player].setEnabled(False)
                    myWindow.personal_field[4].setEnabled(True)
                    acted = ArableExpansion(field)
                    if acted.execute():
                        pprint(acted.log())
                        break
                    pprint(acted.log())
        #         if play is HouseExpansion:
                
        #         if play is ConstructBarn:
                
        #         if play is PlayableSubCardListup:
                
        #         if play is BuySubCard:
                
        #         if play is PlayableJobCardListup:
                
        #         if play is BuyJobCard1:
                
        #         if play is BuyJobCard2:

        #         if play is UseWorker:
                
        # else:
        #     pprint(can.log())

class WidgetrandomRound(QWidget, basic_roundcard_ui) :
    def __init__(self, cardnumber,imagenumber,parent) :
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.parent = parent
        self.cardnum = cardnumber
        self.imagenum = imagenumber
        self.setupUi(self)
        self.btn_round_1.setText('')
        self.btn_round_4.hide()

        if self.cardnum<=3:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/랜덤/랜덤 ({self.imagenum}).png);}}#widget:disabled{{border-image: url(:/newPrefix/images/라운드카드/number_1.png);}}")
        elif self.cardnum<=6:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/랜덤/랜덤 ({self.imagenum}).png);}}#widget:disabled{{border-image: url(:/newPrefix/images/라운드카드/number_2.png);}}")
        elif self.cardnum<=8:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/랜덤/랜덤 ({self.imagenum}).png);}}#widget:disabled{{border-image: url(:/newPrefix/images/라운드카드/number_3.png);}}")
        elif self.cardnum<=10:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/랜덤/랜덤 ({self.imagenum}).png);}}#widget:disabled{{border-image: url(:/newPrefix/images/라운드카드/number_4.png);}}")
        elif self.cardnum<=12:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/랜덤/랜덤 ({self.imagenum}).png);}}#widget:disabled{{border-image: url(:/newPrefix/images/라운드카드/number_5.png);}}")
        elif self.cardnum<=13:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/랜덤/랜덤 ({self.imagenum}).png);}}#widget:disabled{{border-image: url(:/newPrefix/images/라운드카드/number_6.png);}}")
        self.setEnabled(False)
        self.update_state()
    def mousePressEvent(self,event):
        pprint(f"Pressed basic round ID : {self.imagenum}")
        # for act in round_card_command_factory(5)().execute:
        #     act(a, b, c ,[]).execute()
        #     act().log()

        # print(i)
        
    def update_state(self):
        round = self.parent.game_status.now_round
        print(self.imagenum)
        # print(i)
            
        if self.cardnum<=round-1:
            self.setEnabled(self.cardnum<=round-1)
            if self.imagenum<5 and "랜덤/랜덤" in self.styleSheet():
                self.btn_round_1.setText(str(1))
        else:
            self.btn_round_1.setText("")
        if  self.cardnum in [3,6,8,10,12,13]:
            self.btn_round_4.show()
            
class Log_viewer(QDialog,log_viewer_ui):
    def __init__(self,main):
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.log.setText("이 곳은 로그를 표기하는 곳입니다.")
        self.timer = QTimer()
        self.hide()
    def logging(self,text,time=500):
        self.timer.stop()
        self.log.setText(text)
        self.show()
        self.timer.timeout.connect(self.hide)
        self.timer.start(500) 

class WorkerBoard(QWidget, worker_board_ui):
    def __init__(self, parent):
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.setupUi(self)
        self.parent = parent
        for i in range(4):
            getattr(self,f"widget_{i}").setEnabled(False)
    def update_state(self):
        # pprint(f"player{myWindow.game_status.now_turn_player} 번 말 선택")
        for i in range(4):
            getattr(self,f"widget_{i}").setEnabled(True)
        getattr(self,f"widget_{self.parent.game_status.now_turn_player}").setEnabled(False)

        # state = getattr(self,f"widget_{myWindow.game_status.now_turn_player}").isEnabled()
        """
        옵저버에게 status를 전달 받고 라운드카드 활성화 및 안내
        """
        pass

class Check(QWidget, check_ui):
    def __init__(self, parent):
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.setupUi(self)
        self.parent = parent
        self.btn_processing.clicked.connect(self.next_turn)
        self.btn_undo.clicked.connect(self.parent.undo)
    def next_turn(self):
        
        # pf = myWindow.player_status[myWindow.game_status.now_turn_player].farm
        # print(construct_fence.ConstructFence(myWindow.player_status[myWindow.game_status.now_turn_player].farm.field,myWindow.player_status[myWindow.game_status.now_turn_player].farm.vertical_fence,myWindow.player_status[myWindow.game_status.now_turn_player].farm.horizon_fence).execute())
        fence = ConstructFence(myWindow.player_status[myWindow.game_status.now_turn_player].farm.field,myWindow.player_status[myWindow.game_status.now_turn_player].farm.vertical_fence,myWindow.player_status[myWindow.game_status.now_turn_player].farm.horizon_fence)
        # fence_ex = fence.execute()# if log:
        # # barn = construct_barn.ConstructBarn(myWindow.player_status[myWindow.game_status.now_turn_player].farm.field,myWindow.player_status[myWindow.game_status.now_turn_player].farm.vertical_fence,myWindow.player_status[myWindow.game_status.now_turn_player].farm.horizon_fence)
        # # barn_ex = barn.execute()# if log:
        # if fence_ex :
        for i in [0,1,2,3]:
            getattr(self.parent.worker_board,f"widget_{i}").setEnabled(True)
        nowturn = self.parent.game_status.now_turn_player
        self.parent.game_status.now_turn_player = (nowturn+1)%4
        self.parent.game_status.next_turn_player = (nowturn+2)%4
        self.parent.update_state_of_all()
        pprint(f"현재 턴은 {self.parent.game_status.now_turn_player}플레이어 입니다.")

        self.parent.set_undo()
        # else:
        #     pprint(fence.log_text)

    def mousePressEvent(self,event):
        pass

class WidgetTextLog(QWidget, text_log_ui):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
    def mousePressEvent(self,event):
        # 팝업창으로 로그창 크게 보여주기 (중요도 하)
        pass


class WidgetInformation(QWidget, information_ui):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_setting.clicked.connect(self.show_setting) #세팅
        self.btn_card_all.clicked.connect(self.show_card_all) #전체카드
        self.btn_scoreboard.clicked.connect(self.show_scoreboard) #점수표

    def show_setting(self):
        self.setting = Setting(self.parent)
        self.setting.exec_()
    def show_card_all(self):
        self.allcard = AllCard(self.parent)
        self.allcard.exec_()
    def show_scoreboard(self):
        self.scoreboard = Scoreboard(self.parent)
        self.scoreboard.exec_()


class Scoreboard(QDialog, scoreboard_ui):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    def mousePressEvent(self,event):
        self.close()


class FirstCardDistribution(QWidget, card_distribution_ui):
    def __init__(self,  parent,player):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.player = player

        list_sub = [CARD_SUB_CONVERTER[c] for c in self.parent.player_status[player].card.start_sub_card]
        list_job = [CARD_JOB_CONVERTER[c] for c in self.parent.player_status[player].card.start_job_card]
        list_put_sub = [CARD_SUB_CONVERTER[c] for c in self.parent.player_status[player].card.put_sub_card]
        list_put_job = [CARD_JOB_CONVERTER[c] for c in self.parent.player_status[player].card.put_job_card]
        list_put_main = self.parent.player_status[player].card.put_main_card
        for i in range(3):
            getattr(self,f"widget_sub_{i+1}").setStyleSheet(f"border-image: url(:/newPrefix/images/보조 설비/보조설비{list_sub[i]}.png);")
            getattr(self,f"widget_job_{i+1}").setStyleSheet(f"border-image: url(:/newPrefix/images/직업 카드/직업카드{list_job[i]}.png);")
            getattr(self,f"label_sub_{i+1}").setText(str(list_sub[i]))
            getattr(self,f"label_job_{i+1}").setText(str(list_job[i]))

class AllCard(QDialog, allcard_ui):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    def mousePressEvent(self,event):
        self.close()


class Setting(QDialog, setting_ui):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)


class SideBar(QWidget, sidebar_ui):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.checked = ""
        self.btns = ["btn_sheep", "btn_pig", "btn_cow"]
        for name in self.btns:
            getattr(self,name).setStyleSheet(f"QPushButton:checked {{background-color: yellow;border-image: url(:/newPrefix/images/{name.split('_')[-1]}.png);}}QPushButton {{border-image: url(:/newPrefix/images/{name.split('_')[-1]}.png);}}")
            getattr(self,name).clicked.connect(lambda _, name=name :self.btnClick(name))
        for name in ["btn_chg_sheep", "btn_chg_pig", "btn_chg_cow", "btn_chg_vegetable", "btn_trade_grain", "btn_trade_vegetable"]:
            pass


    def btnClick(self, btn_name):
        btns = deepcopy(self.btns)
        btns.remove(btn_name)
        for name in btns:
            getattr(self,name).setChecked(False)
        # getattr(self,btn_name).setChecked(True)
        if getattr(self,btn_name).isChecked():
            self.checked = btn_name
        else: self.checked = ""

    def update_state(self):
        # self.btn.
        pass

        # getattr(self,btn_name).setFocus(False)
        # # 모든 focus 값을 False로 설정
        # self.focus = [False] * len(self.focus)
        # # 클릭된 버튼의 인덱스에 해당하는 focus만 True로 설정
        # self.focus[index] = True
        # print(f"Button {self.btns[index]} clicked. Focus: {self.focus}")

        # addStyleSheet(getattr(self,f"{self.btns[index]}"), "background-color: yellow;")

def addStyleSheet(widget, new_style):
    # 현재 스타일 시트를 가져온다
    current_style = widget.styleSheet()
    # 새로운 스타일 규칙을 추가한다
    updated_style = current_style + '\n' + new_style
    # 업데이트된 스타일 시트를 설정한다
    widget.setStyleSheet(updated_style)
###실행 코드### 밑에 건들 필요 굳이 없음###
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    
    #WindowClass의 인스턴스 생성
    myWindow = MainWindowClass()
    global pprint
    pprint = myWindow.pprint
    update = lambda: myWindow.update_state_of_all()
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()