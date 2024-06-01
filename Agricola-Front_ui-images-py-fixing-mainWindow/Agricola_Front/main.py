import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer

import os
import images_rc
import IMG_0404_rc
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

main = uic.loadUiType(resource_path("mainwindow_v1.ui"))[0] # 진짜 메인
field_base_ui = uic.loadUiType(resource_path("PersonalField/field_base.ui"))[0] # field 하나 ui
personal_field_ui = uic.loadUiType(resource_path("PersonalField/field_frame.ui"))[0] # 농장 15개 빈칸 뚫린 ui
personal_resourcs_ui= uic.loadUiType(resource_path("PersonalField/personal_resource.ui"))[0] # 창 전환되는 자원 창
personal_card_ui= uic.loadUiType(resource_path("PersonalField/personal_card.ui"))[0] # 농장 15개 빈칸 뚫린 ui
basic_roundcard_ui= uic.loadUiType(resource_path("Basic/round_stack.ui"))[0] # 농장 15개 빈칸 뚫린 ui
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
        self.basic_round = [WidgetBasicRound(i,self) for i in range(16)]
        for i in range(16):getattr(self,f"roundCard_{i}").addWidget(self.basic_round[i])


        ####################################init####################################
        self.timer_close,self.timer_open = QTimer(self),QTimer(self)
        self.log.clicked.connect(self.change_main)
        ############################################################################



    def change_main(self):
        currentWidget = self.stackedWidget.currentWidget().objectName()
        # if index == 0:self.stackedWidget.setCurrentIndex(1)
        # else:self.stackedWidget.setCurrentIndex(0)
        if currentWidget == "round":self.change_stacked_page("personal")
        else:self.change_stacked_page("round")



    def change_stacked_page(self,after_page):
        after_page = getattr(self,after_page)
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



class WidgetPersonalField(QWidget, personal_field_ui) :
    def __init__(self, player,parent) :
        super().__init__()
        self.setupUi(self)
        self.player = player
        self.main = parent
        for i in range(15):
            setattr(self, f"field_{i}", self.widgetFieldBase(i,self)) # field_0 ~ field_14 까지
        
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

    class widgetFieldBase(QWidget, field_base_ui) :
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
    def __init__(self, player,parent) :
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.parent = parent
        self.player = player
        self.setupUi(self)
    def mousePressEvent(self,event):
        print(f"Pressed card Player ID : {self.player}")

class WidgetPersonalResource(QWidget, personal_resourcs_ui) :
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

###실행 코드### 밑에 건들 필요 굳이 없음###
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    #WindowClass의 인스턴스 생성
    myWindow = MainWindowClass()
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()