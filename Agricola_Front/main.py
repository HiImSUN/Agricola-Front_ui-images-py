import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os
import images_rc
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
#UI파일 연결
main = uic.loadUiType(resource_path("mainwindow_v3.ui"))[0] # 진짜 메인
#개인 영역 UI들
personal_field_ui = uic.loadUiType(resource_path("PersonalField/field_frame.ui"))[0] # 농장 15개 빈칸 뚫린 ui
field_base_ui = uic.loadUiType(resource_path("PersonalField/field_base.ui"))[0] # field 하나 ui
personal_card_ui= uic.loadUiType(resource_path("PersonalField/mycards.ui"))[0] # 개인 카드 ui
personal_resources_ui= uic.loadUiType(resource_path("PersonalField/personal_resource.ui"))[0] # 창 전환되는 자원 창
#공동 영역 UI들
basic_roundcard_ui= uic.loadUiType(resource_path("Basic/roundcard.ui"))[0] # 라운드카드 ui


# MAIN
class MainWindowClass(QMainWindow, main) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #플레이어 필드 위젯 설정
        self.personal_field = [WidgetPersonalField(i,self) for i in range(4)]
        for i in range(4):
            getattr(self,f"p{i}_0").addWidget(self.personal_field[i])

        #베이직 라운드 위젯 설정
        self.basic_round = [WidgetBasicRound(i,self) for i in range(16)]
        for i in range(16):getattr(self, f"basic_{i+1}").addWidget(self.basic_round[i])
        #라운드 위젯 설정
        self.game_round = []
        for i in range(4):
            self.game_round.append(WidgetBasicRound(i,self))
            getattr(self, f"round1_{i+1}")

# 필드 15개 빈칸 뚫린 개인농장
class WidgetPersonalField(QWidget, personal_field_ui) :
    def __init__(self, player, parent) :
        super().__init__()
        self.setupUi(self)
        self.player = player
        self.main = parent
        # field
        field_list = [setattr(self, f"field_{i}", self.WidgetFieldBase(i,self)) for i in range(15)]
        
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

    # 한 칸의 필드 위젯
    class WidgetFieldBase(QWidget, field_base_ui) :
        def __init__(self, id, parent):
            super().__init__()
            self.setupUi(self)
            self.id = id # field에게 고유 id (0~14) 부여
            self.parent = parent
            self.btn_field_unit.clicked.connect(self.print_id)
        def mousePressEvent(self,event):
            print(f"Pressed Fence Player ID : {self.parent.player} | Fence ID: {self.id}")
        
        def print_id(self):
            print(f"Field ID:{self.parent.player} {self.id}")
            if not self.pushButton_2.isVisible():
                self.pushButton_3.hide()
            self.pushButton_2.hide()

# 창 전환되는 자원 창
class WidgetPersonalResource(QWidget, personal_resources_ui) :
    def __init__(self, player, parent) :
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