import sys,os,copy,random,traceback
# 모듈이 위치한 디렉토리를 지정합니다.
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Agricola_Back/Agricola'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'))
sys.dont_write_bytecode = True # pyc 생성 방지
def custom_exception_handler(exctype, value, tb):
    # 오류 메시지 출력
    # rest_api("beamin_error",Type="PUT",error=str(exctype).replace("'",'"'),beego=str(value).replace("'",'"')+str(traceback))
    print(exctype,value,traceback.format_tb(tb))
    pass
# 기존 예외 핸들러를 저장하고 새 예외 핸들러를 설정
original_exception_handler = sys.excepthook
sys.excepthook = custom_exception_handler
from list_import import *
# run_pyrcc5()#QRC 업데이트/
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
        self.random_card_resource = {"sheep":[1,1],"pig":[1,1],"horse":[1,1],"east":[1,1],"west":[1,1]}
        # self.game_context = GameContext(self.game_status,self.player_status,self.round_status)
        from Agricola_Back.Agricola.gameready import start_resource_distribution,round_card_shuffle
        StartResourceDistribution(self)         # 리소스 할당
        RoundCardShuffle(self)                  # 라운드 카드 할당
        CardDistribution(self)                  # 개인 카드 할당
        self.game_status.now_round+=1
        for i in range(4):
            self.player_status[i].card.start_job_card = deepcopy(self.player_status[i].card.hand_job_card)
            self.player_status[i].card.start_sub_card = deepcopy(self.player_status[i].card.hand_sub_card)
            self.player_status[i].card.put_job_card = deepcopy(self.player_status[i].card.hand_job_card)
            self.player_status[i].card.put_sub_card = deepcopy(self.player_status[i].card.hand_sub_card)
        

#플레이어 필드 위젯 설정
        print("플레이어 필드 위젯 설정중")
        self.personal_field = [WidgetPersonalField(i,self) for i in range(5)]
        for i in range(4):getattr(self,f"frm_p{i}_0").addWidget(self.personal_field[i])
#메인 필드 위젯 설정
        print("#메인 필드 위젯 설정")
        self.frm_main_field.addWidget(self.personal_field[4])
        for j in [1,3,5,7,9]:
            for lay in ["horizontalLayout_A","horizontalLayout_B","horizontalLayout_A_5",]:
                getattr(self.personal_field[4],lay).setStretch(j,6)
                                    # self.personal_field[4].verticalLayout_2.setStretch(j,1)
                                # self.personal_field[4].horizontalLayout_A.setStretch(10,2)
#플레이어 카드 위젯 설정
        print("#플레이어 카드 위젯 설정")
        self.personal_card = [PersonalCard_small(i,self) for i in range(4)]
        for i in range(4):getattr(self,f"frm_p{i}_1").addWidget(self.personal_card[i])
#메인 카드 위젯 설정
        print("#메인 카드 위젯 설정")
        self.main_card = [PersonalCard_big(self,player) for player in range(4)]
        for i in range(4):
            getattr(self,f"main_card__{i}").addWidget(self.main_card[i])
#사이드바 위젯 설정
        print("사이드바 위젯 설정")
        self.sidebar = SideBar(self)
        self.frm_main_sidebar.addWidget(self.sidebar)
        
#플레이어 리소스 위젯 설정
        print("플레이어 리소스 위젯 설정")
        self.personal_resource = [WidgetPersonalResource(i,self) for i in range(4)]
        for i in range(4):getattr(self,f"frm_p{i}_2").addWidget(self.personal_resource[i])
#베이직 라운드 위젯 설정
        print("베이직 라운드 위젯 설정")
        self.basic_round = [WidgetBasicRound(i,self) for i in range(16)]
        [getattr(self,f"basic_{i}").addWidget(self.basic_round[i]) for i in range(16)]
# 랜덤위젯 설정
        print("랜덤위젯 설정")
        # for i, order in enumerate(self.game_status.round_card_order):
        #     self.game_status.round_resource[i] -= order
        # 라운드순서배정결과 = [1, 2, 0, 3, 5, 6, 4, 8, 7, 10, 9, 12, 11, 13]
        # print(self.game_status.round_resource)
        # print("self.game_status.round_card_order",self.game_status.round_card_order)
        for i in range(len(self.game_status.round_card_order)):
            if self.game_status.round_card_order[i] == 1:
                self.random_card_resource["sheep"] = [-i+1,1]
            elif self.game_status.round_card_order[i] == 5:
                self.random_card_resource["east"] = [-i+1,1]
            elif self.game_status.round_card_order[i] == 7:
                self.random_card_resource["pig"] = [-i+1,1]
            elif self.game_status.round_card_order[i] == 9:
                self.random_card_resource["horse"] = [-i+1,1]
            elif self.game_status.round_card_order[i] == 10:
                self.random_card_resource["west"] = [-i+1,1]
                
                
        print(self.game_status.round_resource)
        self.round_round = [WidgetrandomRound(i,self.game_status.round_card_order[i],self) for i in range(14)]
        [getattr(self,f"basic_{i+16}").addWidget(self.round_round[i]) for i in range(14)]
#워커보드 설정
        print("워커보드 설정")
        self.worker_board = WorkerBoard(self)
        self.vlo_etc_workerboard.addWidget(self.worker_board)
#인포메이션 칸(설정, 점수표)

        print("인포메이션 칸(설정, 점수표)")
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
        self.set_undo()
        ############################################################################
        self.stackedWidget.setCurrentIndex(2) # 게임시작 화면
        self.GAMESTART_BUTTON.clicked.connect(self.game_start)

        #카드 확인하면 다음사람에게 넘기기
        print("")
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
        # self.next_round()
        self.open()
        self.update_state_of_check()

        self.update_state_of_all()




    def play_sound(self):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),f'data/media/strongcowsound.mp3')  # 절대 경로로 변경
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
        self.stackedWidget.setCurrentIndex(3) #player1의 카드 공개




    def game_start(self):
        pprint("게임이 시작되었습니다.")
        self.play_sound()
        











        
    def round_test(self):
        self.game_status.now_round = (self.game_status.now_round+1)%15
        pprint(f"현재 라운드는 {self.game_status.now_round}라운드입니다.")
        self.next_round()
        self.update_state_of_all()
        [getattr(self,f"basic_{i+16}").addWidget(self.round_round[i]) for i in range(13)]
        

    def set_undo(self):
        self.undo_player = deepcopy(self.player_status)
        self.hand_undo_gameStatus = deepcopy(self.game_status)
        self.undo_round = deepcopy(self.round_status)
        
    def undo(self):
        self.player_status = self.undo_player
        self.game_status = self.hand_undo_gameStatus
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

    def change_main_stacked(self):
        self.update_state_of_all()
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


    def update_main_personal_field(self):
        for c in self.personal_field[:-1]:
            c.update_state()
            for cc in c.field: cc.update_state()
    def update_main_personal_resource(self):
        for c in self.personal_resource:
            c.update_state()
    def update_main_presonal_card(self):
        for widget in self.personal_card:
            widget.update_state()
        
    def update_main_main_field(self):
            self.personal_field[-1].update_state()
            for cc in self.personal_field[-1].field: cc.update_state()
    def update_main_round(self):
        for widget in self.round_round:
            widget.update_state()
    def update_main_card(self):
        for widget in self.main_card:
            widget.update_state()
    

    def update_state_of_check(self):  
        self.update_main_personal_field()
        self.update_main_personal_resource()
        self.update_state_of_all()


    def update_state_of_all(self):
        # self.update_main_personal_field()
        self.update_main_presonal_card()
        #self.update_main_personal_resource()
        self.update_main_main_field()
        self.update_main_round()
        self.update_main_card()
        self.worker_board.update_state()
        self.update_state()




    def next_round(self):
        # stack_resources(self.game_status)
        for name,d in self.random_card_resource.items():
            self.random_card_resource[name]=[d[0]+d[1],d[1]]
        pass





























class WidgetPersonalField(QWidget, personal_field_ui) :
    def __init__(self, player,parent) :
        super().__init__()
        self.setupUi(self)
        self.player = player
        self.parent = parent
        self.field = [WidgetFieldBase(i,self) for i in range(15) ]# field_0 ~ field_14 까지
        
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
                    getattr(self, f'btn_fence_h{j}{i}').clicked.connect(self.parent.change_main_stacked)
                    getattr(self, f'btn_fence_h{j}{i}').setCheckable(False)
            for j in range(3):
                for i in range(6):
                    getattr(self, f'btn_fence_v{j}{i}').clicked.connect(self.parent.change_main_stacked)
                    getattr(self, f'btn_fence_v{j}{i}').setCheckable(False)

    def mousePressEvent(self,event):
        pprint(f"Pressed personalField Player ID : {self.player}")
        if self.player != 4:
            self.parent.change_main_stacked()            
    
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
            player = self.parent.game_status.now_turn_player
        else:
            player = self.player
        # self.setEnabled(player == self.parent.game_status.now_turn_player)
        
        # 펜스 state
        for j in range(4):
            for i in range(5):
                if self.parent.player_status[player].farm.horizon_fence[j][i] == True:
                    getattr(self, f'btn_fence_h{j}{i}').setStyleSheet(f"border:0.5px solid rgba(255, 255, 255, 128);border-image : url(:/newPrefix/images/fence_h_{player}.png);")
                else:
                    getattr(self, f'btn_fence_h{j}{i}').setStyleSheet("border:0.5px solid rgba(255, 255, 255, 128);border-image : none;")
        for j in range(3):
            for i in range(6):
                if self.parent.player_status[player].farm.vertical_fence[j][i] == True:
                    getattr(self, f'btn_fence_v{j}{i}').setStyleSheet(f"border:0.5px solid rgba(255, 255, 255, 128);border-image : url(:/newPrefix/images/fence_v_{player}.png);")
                else:
                    getattr(self, f'btn_fence_v{j}{i}').setStyleSheet("border:0.5px solid rgba(255, 255, 255, 128);border-image : none;")

class WidgetFieldBase(QWidget, field_base_ui) :
    def __init__(self, id,parent):
        super().__init__()
        self.setupUi(self)
        self.id = id # field에게 고유 id (0~14) 부여
        self.i = self.id//5
        self.j = self.id%5
        self.parent = parent
        self.player = self.parent.player
        if self.player == 4:
            self.btn_unit.clicked.connect(self.change_unit)
            self.btn_barn.clicked.connect(self.change_barn)
        else:
            self.btn_unit.clicked.connect(self.parent.parent.change_main_stacked)
            self.btn_barn.clicked.connect(self.parent.parent.change_main_stacked)
          
    def mousePressEvent(self,event):
        if self.player != 4:
            self.parent.parent.change_main_stacked()
        else:
            pprint(f"Pressed Fance Player ID : {self.parent.player} |  ID: {self.id}")
            self.change_house ()
            myWindow.player_status[myWindow.game_status.now_turn_player].farm.field[self.i][self.j].count+=1
            myWindow.update_state_of_all()

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
        # self.vertical_fence=myWindow.player_status[player].farm.vertical_fence
        # self.horizontal_fence=myWindow.player_status[player].farm.horizon_fence
        # myWindow.player_status[player].farm.field[self.i][self.j].kind = rand[0]
        print(self.parent.parent.sidebar.checked)
        if True:
            print(myWindow.player_status[player].farm.field[self.i][self.j].field_type)
            if str(myWindow.player_status[player].farm.field[self.i][self.j].field_type) == str(FieldType.HOUSE):
                pprint("집 위에는 둘 수 없습니다.")
            else:
                if self.parent.parent.sidebar.checked:
                    Type = CropType if self.parent.parent.sidebar.checked.split('_')[-1].upper() in TYPE_Crop else AnimalType
                    if myWindow.player_status[myWindow.game_status.now_turn_player].farm.field[self.i][self.j].kind != self.parent.parent.sidebar.checked.split('_')[-1].upper() and myWindow.player_status[myWindow.game_status.now_turn_player].farm.field[self.i][self.j].kind != None:
                        pprint("같은 종류만 둘 수 있습니다.")
                    else:
                        myWindow.player_status[myWindow.game_status.now_turn_player].farm.field[self.i][self.j].kind = self.parent.parent.sidebar.checked.split('_')[-1].upper()
                        getattr(myWindow.sidebar,f"btn_{self.parent.parent.sidebar.checked.split('_')[-1]}_count").setText(f"x{int(getattr(myWindow.sidebar,f"btn_{self.parent.parent.sidebar.checked.split('_')[-1]}_count").text().replace("x",""))-1}")
                        if Type == AnimalType:       
                            myWindow.player_status[myWindow.game_status.now_turn_player].farm.field[self.i][self.j].count+=1
                        else:
                            count = getattr(myWindow.player_status[myWindow.game_status.now_turn_player].resource,self.parent.parent.sidebar.checked.split('_')[-1])
                            setattr(myWindow.player_status[myWindow.game_status.now_turn_player].resource,self.parent.parent.sidebar.checked.split('_')[-1],count+1)
                            print(f"btn_{self.parent.parent.sidebar.checked.split('_')[-1]}_count")
                        if getattr(myWindow.sidebar,f"btn_{self.parent.parent.sidebar.checked.split('_')[-1]}_count").text()=="x0":
                            myWindow.sidebar.btn_disabled()
                else: 
                    kind = str(myWindow.player_status[player].farm.field[self.i][self.j].kind).lower()
                    if kind != "none":
                        count = int(getattr(myWindow.sidebar,f"btn_{kind}_count").text().replace("x",""))
                        Type = CropType if kind in TYPE_Crop else AnimalType
                        if Type == AnimalType:
                            if myWindow.player_status[player].farm.field[self.i][self.j].count>0:
                                myWindow.player_status[player].farm.field[self.i][self.j].count-=1
                                getattr(myWindow.sidebar,f"btn_{kind}_count").setText(f"x{int(getattr(myWindow.sidebar,f"btn_{kind}_count").text().replace("x",""))+1}")
                                
                                
                            if myWindow.player_status[player].farm.field[self.i][self.j].count==0:
                                myWindow.player_status[player].farm.field[self.i][self.j].kind = None
                        else:
                            count = str(getattr(myWindow.sidebar,f"btn_{kind}_count").text()[1:])
                            if count>0:
                                setattr(myWindow.player_status[myWindow.game_status.now_turn_player].resource,self.parent.parent.sidebar.checked.split('_')[-1],count-1)
                                getattr(myWindow.sidebar,f"btn_{kind}_count").setText(f"x{int(getattr(myWindow.sidebar,f"btn_{kind}_count").text().replace("x",""))+1}")


                            if count == 1:
                                myWindow.player_status[player].farm.field[self.i][self.j].kind = None


        myWindow.update_state_of_all()
        myWindow.update_state_of_check()

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
            kind = self.parent.parent.player_status[player].farm.field[self.i][self.j].kind.lower()
            if not kind == "none":
                self.btn_unit.setStyleSheet(f"#btn_unit{{border-image : url(:/newPrefix/images/{self.parent.parent.player_status[player].farm.field[self.i][self.j].kind.lower()}.png);}}")
            else:
                self.btn_unit.setStyleSheet(f"#btn_unit{{border:none;}}")
        else:
            self.btn_unit.setStyleSheet(f"#btn_unit{{border:none;}}")
        count = self.parent.parent.player_status[player].farm.field[self.i][self.j].count if self.parent.parent.player_status[player].farm.field[self.i][self.j].count not in [0,None] else ""
        if count == "" and self.parent.parent.player_status[player].farm.field[self.i][self.j].kind!= None:
            count = getattr(self.parent.parent.player_status[self.parent.parent.game_status.now_turn_player].resource,self.parent.parent.player_status[player].farm.field[self.i][self.j].kind.lower())
        if count == 0:
            count = ""
        self.count.setText(str(count))
        # 외양간 처리
        if self.parent.parent.player_status[player].farm.field[self.i][self.j].barn:
            styleSheet = f"QPushButton#btn_barn {{border-image: url(:/newPrefix/images/barn_{player}.png);}}"
        else:
            styleSheet = f"QPushButton#btn_barn {{border: none;}}"
        self.btn_barn.setStyleSheet(styleSheet)

        pass
        
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
            # print(f"#widget_job_{i+1}{{border-image: url(:/newPrefix/images/직업 카드/직업카드{list_job[i]}.png);}}#widget_sub_{i+1}:disabled{{border-image: url(:/newPrefix/images/직업 카드/직업카드back.png);}}")
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
        # print(list_job,list_put_job,list_job[0] not in list_put_job)
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
            
            # print(f"#widget_job_{i+1}{{border-image: url(:/newPrefix/images/직업 카드/직업카드{list_job[i]}.png);}}#widget_sub_{i+1}:disabled{{border-image: url(:/newPrefix/images/직업 카드/직업카드back.png);}}")
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
        # print(list_job,list_put_job,list_job[0] not in list_put_job)
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
            # print("cow = ",getattr(self.parent.player_status[player].farm,f"get_cow_count")())

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

    def mousePressEvent(self,event):
        pprint(f"Pressed basic round num : {self.num}")

class WidgetrandomRound(QWidget, basic_roundcard_ui) :
    def __init__(self, cardnumber,imagenumber,parent) :
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.parent = parent
        self.cardnum = cardnumber
        self.imagenum = imagenumber
        self.setupUi(self)
        self.btn_round_1.setText('')
        # self.btn_round_1.hide()
        self.btn_round_4.hide()

        if self.cardnum<=3:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/랜덤/랜덤 ({self.imagenum}).png);}}#widget:disabled{{border-image: url(:/newPrefix/images/라운드카드/number_1.png);}}#btn_round_1:disabled{{color:rgba(255, 255, 255, 0);}}")
        elif self.cardnum<=6:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/랜덤/랜덤 ({self.imagenum}).png);}}#widget:disabled{{border-image: url(:/newPrefix/images/라운드카드/number_2.png);}}#btn_round_1:disabled{{color:rgba(255, 255, 255, 0);}}")
        elif self.cardnum<=8:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/랜덤/랜덤 ({self.imagenum}).png);}}#widget:disabled{{border-image: url(:/newPrefix/images/라운드카드/number_3.png);}}#btn_round_1:disabled{{color:rgba(255, 255, 255, 0);}}")
        elif self.cardnum<=10:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/랜덤/랜덤 ({self.imagenum}).png);}}#widget:disabled{{border-image: url(:/newPrefix/images/라운드카드/number_4.png);}}#btn_round_1:disabled{{color:rgba(255, 255, 255, 0);}}")
        elif self.cardnum<=12:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/랜덤/랜덤 ({self.imagenum}).png);}}#widget:disabled{{border-image: url(:/newPrefix/images/라운드카드/number_5.png);}}#btn_round_1:disabled{{color:rgba(255, 255, 255, 0);}}")
        elif self.cardnum<=13:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/랜덤/랜덤 ({self.imagenum}).png);}}#widget:disabled{{border-image: url(:/newPrefix/images/라운드카드/number_6.png);}}#btn_round_1:disabled{{color:rgba(255, 255, 255, 0);}}")
        self.setEnabled(False)

    def mousePressEvent(self,event):
        pprint(f"Pressed basic round ID : {self.imagenum}")
        if self.imagenum == 0:    
            SheepMarket(myWindow)
        if self.imagenum == 1:
            SheepMarket(myWindow)
        if self.imagenum == 2:
            print(Facilities(myWindow))
        if self.imagenum == 3:
            print(SeedBake(myWindow))
        if self.imagenum == 4:
            print(FamilyFacility(myWindow))
        if self.imagenum == 5:
            print(Stone2(myWindow))
        if self.imagenum == 6:
            print(UpgradeFacilities(myWindow))
        if self.imagenum == 7:
            print(PigMarket(myWindow))
        if self.imagenum == 8:
            print(VegetableSeed(myWindow))
        if self.imagenum == 9:
            print(CowMarket(myWindow))
        if self.imagenum == 10:
            print(Stone4(myWindow))
        if self.imagenum == 11:
            print(CultivateSeed(myWindow))
        if self.imagenum == 12:
            print(HurryFamily(myWindow))
        if self.imagenum == 13:
            print(UpgradeFence(myWindow))
        # print(i)
        
    def update_state(self):
        round = self.parent.game_status.now_round
        # print("current_found = ",round)
        # print(self.imagenum)
        # print(i)
        
        if self.cardnum<=round-1:
            self.setEnabled(self.cardnum<=round-1)
        if self.imagenum in [1, 5, 7, 9, 10] :
            if self.imagenum == 1  :
                self.btn_round_1.setText(str(self.parent.random_card_resource["sheep"][0]))
            elif self.imagenum == 5 :
                self.btn_round_1.setText(str(self.parent.random_card_resource["east"][0]))
            elif self.imagenum == 7 :
                self.btn_round_1.setText(str(self.parent.random_card_resource["pig"][0]))
            elif self.imagenum == 9 :
                self.btn_round_1.setText(str(self.parent.random_card_resource["horse"][0]))
            elif self.imagenum == 10 :
                self.btn_round_1.setText(str(self.parent.random_card_resource["west"][0]))
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
        from Agricola_Back.Agricola.behavior.basebehavior.construct_fence import ConstructFence
        
        fence_test = fence_validation(self.parent)
        print(fence_test)
        import pickle

        data = [myWindow.player_status,myWindow.game_status,myWindow.round_status]
        with open(r'C:\Users\js000\OneDrive\문서\GitHub\Agricola-Front_ui-images-py\Agricola_Front\main.pkl', 'wb') as file:
            pickle.dump(data, file)
        fence = ConstructFence(myWindow.player_status[myWindow.game_status.now_turn_player].farm.field,myWindow.player_status[myWindow.game_status.now_turn_player].farm.vertical_fence,myWindow.player_status[myWindow.game_status.now_turn_player].farm.horizon_fence,myWindow)
        fence_ex = fence.execute()# if log:
        print(fence_ex)
        print(fence.log())

        if fence_ex:
            # pf = myWindow.player_status[myWindow.game_status.now_turn_player].farm
            # print(ConstructFence(myWindow.player_status[myWindow.game_status.now_turn_player].farm.field,myWindow.player_status[myWindow.game_status.now_turn_player].farm.vertical_fence,myWindow.player_status[myWindow.game_status.now_turn_player].farm.horizon_fence).execute())
            # barn = construct_barn.ConstructBarn(myWindow.player_status[myWindow.game_status.now_turn_player].farm.field,myWindow.player_status[myWindow.game_status.now_turn_player].farm.vertical_fence,myWindow.player_status[myWindow.game_status.now_turn_player].farm.horizon_fence)
            # # barn_ex = barn.execute()# if log:
            # if fence_ex :
            for i in [0,1,2,3]:
                getattr(self.parent.worker_board,f"widget_{i}").setEnabled(True)
            nowturn = self.parent.game_status.now_turn_player
            self.parent.game_status.now_turn_player = (nowturn+1)%4
            self.parent.game_status.next_turn_player = (nowturn+2)%4
            self.parent.update_state_of_all()
            pprint(f"현재 턴은 {self.parent.game_status.now_turn_player}플레이어 입니다.")
            myWindow.update_state_of_check()
            self.parent.set_undo()
            # else:
            #     pprint(fence.log_text)
        else:
            pprint(str(fence.log()))
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
        self.btns = ["btn_sheep", "btn_pig", "btn_cow", "btn_vegetable", "btn_grain"]
        for name in self.btns:
            getattr(self,name).setStyleSheet(f"QPushButton:checked {{background-color: yellow;border-image: url(:/newPrefix/images/{name.split('_')[-1]}.png);}}QPushButton {{border-image: url(:/newPrefix/images/{name.split('_')[-1]}.png);}}")
            getattr(self,name).clicked.connect(lambda _, name=name :self.btnClick(name))
        for name in ["btn_chg_sheep", "btn_chg_pig", "btn_chg_cow", "btn_chg_vegetable", "btn_trade_grain", "btn_trade_vegetable"]:
            pass


    def btnClick(self, btn_name):
        btns = deepcopy(self.btns)
        if not getattr(self,btn_name+"_count").text() == "x0":
            btns.remove(btn_name)
            for name in btns:
                getattr(self,name).setChecked(False)
            # getattr(self,btn_name).setChecked(True)
            if getattr(self,btn_name).isChecked():
                self.checked = btn_name
            else: self.checked = False
        else:
            for name in btns:
                getattr(self,name).setChecked(False)
                self.checked = False
    def btn_disabled(self):
        for name in self.btns:
            getattr(self,name).setChecked(False)
        self.checked = False
    def update_state(self):
        # self.label_2_sheepcount
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