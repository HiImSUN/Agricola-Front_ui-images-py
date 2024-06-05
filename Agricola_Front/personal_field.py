import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os
import data.images_rc as images_rc
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

personal_field_ui = uic.loadUiType(resource_path("PersonalField/field_frame.ui"))[0] # 농장 15개 빈칸 뚫린 ui
main = uic.loadUiType(resource_path("PersonalField/main.ui"))[0] # main ui 불러오고
field_base_ui = uic.loadUiType(resource_path("PersonalField/field_base.ui"))[0] # field 하나 ui
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
# field_0_ui
#  = uic.loadUiType("main.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class MainWindowClass(QMainWindow, main) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #self.????.clicked.connect(lambda :print_hello(self))

        # field
        self.personal_field = widgetPersonalFieldClass()
        #field_list = []
        for i in range(15):
            setattr(self, f"field_{i}", widgetFieldBase(i)) # field_0 ~ field_14 까지
            #field_list.append(getattr(self, f"field_{i}"))
        
        self.main.addWidget(self.personal_field)
        tmp_field_num = 0
        for i in range(3):
            for j in range(5):
                field = getattr(self, f'field_{tmp_field_num}')
                layout_name = f'hlo_{i}_{j}'
                layout = getattr(self.personal_field, layout_name)
                layout.addWidget(field)
                tmp_field_num += 1

        # fence 객체들에 대하여 버튼 클릭 이벤트 추가
        for i in range(38):
            btn = getattr(self.personal_field, f'btn_fence_{i}')
            btn.clicked.connect(lambda _, id=i: self.personal_field.print_id(id))

class widgetPersonalFieldClass(QWidget, personal_field_ui) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    def print_id(self, id):
        print(f"Fence ID: {id}")

class widgetFieldBase(QWidget, field_base_ui) :
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.id = id # field에게 고유 id (0~14) 부여
        self.btn_field_unit.clicked.connect(self.print_id)

    def print_id(self):
        print(f"Field ID: {self.id}")

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