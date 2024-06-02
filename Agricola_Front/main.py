import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
import os
import MyQRC_rc

import sys
import os

# 모듈이 위치한 디렉토리를 지정합니다.
module_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Agricola_Back')
# sys.path에 모듈 디렉토리를 추가합니다.
if module_dir not in sys.path:
    sys.path.append(module_dir)
from Agricola_Back.repository import player_status_repository,game_status_repository,round_status_repository,undo_repository



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
#UI파일 연결
main = uic.loadUiType(resource_path("mainwindow_v1.ui"))[0] # 진짜 메인
###개인 영역 UI들###
personal_field_ui = uic.loadUiType(resource_path("PersonalField/field_frame.ui"))[0] # 농장 15개 빈칸 뚫린 ui
field_base_ui = uic.loadUiType(resource_path("PersonalField/field_base.ui"))[0] # field 하나 ui
personal_resources_ui= uic.loadUiType(resource_path("PersonalField/personal_resource.ui"))[0] # 화면 전환되는 개인 자원
personal_card_ui= uic.loadUiType(resource_path("PersonalField/personal_card.ui"))[0] # 내가 낸 카드 ui
#personal_card_ui= uic.loadUiType(resource_path("PersonalField/mycards.ui"))[0] # 개인 카드 ui

###공동 영역 UI들###
log_viewer_ui= uic.loadUiType(resource_path("log_viewer_dialog.ui"))[0] # 로그
basic_roundcard_ui= uic.loadUiType(resource_path("Basic/roundcard.ui"))[0] # 라운드카드 ui
worker_board_ui = uic.loadUiType(resource_path("Basic/worker_board.ui"))[0] # worker 보드
check_ui = uic.loadUiType(resource_path("check/check.ui"))[0] # worker 보드
text_log_ui = uic.loadUiType(resource_path("Basic/log.ui"))[0] # text log 박스
information_ui = uic.loadUiType(resource_path("Basic/information.ui"))[0] # information(설정, 점수표)
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
# field_0_ui
#  = uic.loadUiType("main.ui")[0]

# MAIN
class MainWindowClass(QMainWindow, main) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #플레이어 필드 위젯 설정
        self.personal_field = [WidgetPersonalField(i,self) for i in range(4)]
        for i in range(4):getattr(self,f"frm_p{i}_0").addWidget(self.personal_field[i])
        #메인 필드 위젯 설정
        self.main_field = WidgetPersonalField(5,self)
        self.frm_main_field.addWidget(self.main_field)
        #플레이어 카드 위젯 설정
        self.personal_card = [WidgetPersonalCard(i,self) for i in range(4)]
        for i in range(4):getattr(self,f"frm_p{i}_1").addWidget(self.personal_card[i])

        #메인 카드 위젯 설정
        self.main_card = WidgetPersonalCard(5,self)
        self.frm_main_card.addWidget(self.main_card)
        #플레이어 리소스 위젯 설정
        self.personal_resource = [WidgetPersonalResource(i,self) for i in range(4)]
        for i in range(4):getattr(self,f"frm_p{i}_2").addWidget(self.personal_resource[i])
        #베이직 라운드 위젯 설정
        self.basic_round = [WidgetBasicRound(i,self) for i in range(30)]
        for i in range(30):getattr(self,f"basic_{i}").addWidget(self.basic_round[i])
        #말칸
        self.worker_board = WorkerBoard(self)
        self.vlo_etc_workerboard.addWidget(self.worker_board)
        #텍스트 로그 창 설정
        self.text_log = WidgetTextLog(self)
        self.vlo_etc_log.addWidget(self.text_log)
        #인포메이션 칸(설정, 점수표)
        self.information = WidgetInformation(self)
        self.vlo_etc_information.addWidget(self.information)

        self.Class_check = Check(self)
        self.verticalLayout_37.addWidget(self.Class_check)
        ####################################init####################################
        self.timer_close,self.timer_open = QTimer(self),QTimer(self)
        self.log.clicked.connect(self.change_main_stacked)
        # self.log_2.clicked.connect(lambda:self.logging_dialog("한번 오류를 볼까요?"))
        # self.log = Log_viewer(self)

        self.player = player_status_repository.PlayerStatusRepository()
        self.gameStatus = game_status_repository.GameStatusRepository()
        self.round = round_status_repository.RoundStatusRepository()
        print(self.player.player_status[0].worker)
        self.pushButton_3.clicked.connect(self.test)
        ############################################################################
    def test(self):
        self.player.player_status[0].resource.stone+=1
        update()

    # def logging_dialog(self,text):
    #     self.log.logging(text)
    #     update()

    def change_main_stacked(self):
        currentWidget = self.stackedWidget.currentWidget().objectName()
        # if index == 0:self.stackedWidget.setCurrentIndex(1)
        # else:self.stackedWidget.setCurrentIndex(0)
        if currentWidget == "round_page":self.change_stacked_page("personal_page")
        else:self.change_stacked_page("round_page")



    def change_stacked_page(self, after_page):
        after_page = getattr(self, after_page)
        stacked_Widget = self.stackedWidget
        if not self.timer_close.isActive() and not self.timer_open.isActive():
            # 이걸로 속도 조절 낮을수록 빠름
            self.speed = 5
            self.timer_close = QTimer(self)
            self.timer_open = QTimer(self)
            self.total_timer_count = 20
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
            self.opacity_effect.setOpacity(1-0.05*self.current_timer_count)
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
            self.opacity_effect_after.setOpacity(1-0.05*self.current_timer_count)
            after_page.setGraphicsEffect(self.opacity_effect_after)
            self.current_timer_count -= 1
            if self.current_timer_count == 0:
                self.timer_open.stop()

    def update_state_of_all(self):
        print("상황판을 업데이트 합니다.")
        #resource 업데이트
        for player in range(4):
            for t in ["dirt","grain","meal","reed","stone","vegetable","wood"]:
                # self.personal_resource[player].count_dirt.setText(str(self.player.player_status[player].resource.dirt))
                getattr(self.personal_resource[player],f"count_{t}").setText(str(getattr(self.player.player_status[player].resource,t)))
        #현재턴만 활성화
        print(f"현재 턴은 {self.gameStatus.game_status.now_turn_player}플레이어 입니다.")
        player_list = [0,1,2,3]
        player_list.remove(self.gameStatus.game_status.now_turn_player)
        for i in player_list:
            self.personal_resource[i].setEnabled(False)
            self.personal_card[i].setEnabled(False)
            self.personal_field[i].setEnabled(False)


class WidgetPersonalField(QWidget, personal_field_ui) :
    def __init__(self, player,parent) :
        super().__init__()
        self.setupUi(self)
        self.player = player
        self.main = parent
        for i in range(15):
            setattr(self, f"field_{i}", self.WidgetFieldBase(i,self)) # field_0 ~ field_14 까지
        
        tmp_field_num = 0
        for i in range(3):
            for j in range(5):
                field = getattr(self, f'field_{tmp_field_num}')
                layout_name = f'hlo_{i}_{j}'
                layout = getattr(self, layout_name)
                layout.addWidget(field)
                tmp_field_num += 1

        # fence 객체들에 대하여 버튼 클릭 이벤트 추가
        for i in range(38):
            btn = getattr(self, f'btn_fence_{i}')
            btn.clicked.connect(lambda _, id=i: self.print_id(id))
    
    def print_id(self, id):
        print(f"Player ID : {self.player} | Fence ID: {id}")
        print(self.objectName())

    class WidgetFieldBase(QWidget, field_base_ui) :
        def __init__(self, id,parent):
            super().__init__()
            self.setupUi(self)
            self.id = id # field에게 고유 id (0~14) 부여
            self.parent = parent
            self.btn_field_unit.clicked.connect(self.print_id)
        def mousePressEvent(self,event):
            print(f"Pressed Fance Player ID : {self.parent.player} | Fence ID: {self.id}")

        def print_id(self):
            print(f"Player ID : {self.parent.player} | Fence ID: {self.id}")
            if not self.pushButton_2.isVisible():
                self.pushButton_3.hide()
            self.pushButton_2.hide()

class WidgetPersonalCard(QWidget, personal_card_ui) :
    def __init__(self, player, parent) :
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        # self.parent
        self.parent = parent
        self.player = player
        self.setupUi(self)
        self.pushButton_1.clicked.connect(lambda : self.plus("dirt"))
        self.pushButton_2.clicked.connect(lambda : self.plus("grain"))
        self.pushButton_3.clicked.connect(lambda : self.plus("meal"))
        self.pushButton_4.clicked.connect(lambda : self.plus("reed"))
    def plus(self, object):
        count = getattr(self.parent.player.player_status[self.player].resource, object)
        setattr(self.parent.player.player_status[self.player].resource, object,count+1)



    def mousePressEvent(self,event):
        print(f"Pressed card Player ID : {self.player}")

class WidgetPersonalResource(QWidget, personal_resources_ui) :
    def __init__(self, player,parent) :
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.setupUi(self)
        self.player = player
        self.parent = parent
    def mousePressEvent(self,event):
        print(f"Pressed Resource Player ID : {self.player}")
        index = self.stackedWidget.currentIndex()
        if index == 0:self.stackedWidget.setCurrentIndex(1)
        else:self.stackedWidget.setCurrentIndex(0)

class WidgetBasicRound(QWidget, basic_roundcard_ui) :
    def __init__(self, round,parent) :
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.parent = parent
        self.round = round
        self.setupUi(self)
    def mousePressEvent(self,event):
        print(f"Pressed basic round ID : {self.round}")




class Log_viewer(QDialog,log_viewer_ui):
    def __init__(self,main):
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.log.setText("이 곳은 로그를 표기하는 곳입니다.")
        self.hide()
    def logging(self,text):
        self.log.setText(text)
        self.show()
        QTimer.singleShot(3000, self.hide)

class WorkerBoard(QWidget, worker_board_ui):
    def __init__(self, parent):
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.setupUi(self)
        self.parent = parent
    def mousePressEvent(self,event):
        """
        옵저버에게 status를 전달 받고 라운드카드 활성화 및 안내
        """
        pass
class Check(QWidget, check_ui):
    def __init__(self, parent):
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.setupUi(self)
        self.parent = parent
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

    def setting(self):
        pass
    def show_scoreboard(self):
        pass

###실행 코드### 밑에 건들 필요 굳이 없음###
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    #WindowClass의 인스턴스 생성
    myWindow = MainWindowClass()
    update = lambda: myWindow.update_state_of_all()
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()