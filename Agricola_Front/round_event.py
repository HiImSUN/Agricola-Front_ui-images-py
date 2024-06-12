# from Agricola_Back.Agricola.behavior.roundbehavior.sheep_market import SheepMarket
def SheepMarket(self):
    self.play_sound("sheep")
    self.pprint(f"양 {self.random_card_resource["sheep"][0]}마리를 획득하였습니다.")
    # self.sidebar.btn_sheep_count.setText(str(self.random_card_resource["sheep"][0]))
    self.sidebar.btn_sheep_count.setText(f"x{int(self.sidebar.btn_sheep_count.text()[1:])+self.random_card_resource["sheep"][0]}")
    self.change_main_stacked()
    self.random_card_resource["sheep"][0] = 0

    # ret = [PlaceAnimal,GainAnimal(AnimalType.SHEEP, self.game_status.round_resource[sheep_card_index]), UseWorker]
def Wood(self,i):
    self.play_sound("ding")
    self.pprint(f"나무 {self.basic_card_resource[i][0]}개를 획득하였습니다.")
    self.player_status[self.game_status.now_turn_player].resource.wood+=self.basic_card_resource[i][0]
    self.basic_card_resource[i][0] = 0

def reed(self,i):
    self.play_sound("ding")
    self.pprint(f"갈대 {self.basic_card_resource[i][0]}개를 획득하였습니다.")
    self.player_status[self.game_status.now_turn_player].resource.reed+=self.basic_card_resource[i][0]
    self.basic_card_resource[i][0] = 0

def get_basic_resource(self,i,name,eng):
    self.play_sound("ding")
    self.pprint(f"{name} {self.basic_card_resource[i][0]}개를 획득하였습니다.")
    setattr(self.player_status[self.game_status.now_turn_player].resource,eng,getattr(self.player_status[self.game_status.now_turn_player].resource,eng)+self.basic_card_resource[i][0])
    self.basic_card_resource[i][0] = 0

def get_random_resource(self,i,name,eng):
    self.play_sound("ding")
    self.pprint(f"{name} {self.random_card_resource[i][0]}개를 획득하였습니다.")
    setattr(self.player_status[self.game_status.now_turn_player].resource,eng,getattr(self.player_status[self.game_status.now_turn_player].resource,eng)+self.random_card_resource[i][0])
    if self.random_card_resource[i][1]>0:
        self.random_card_resource[i][0] = 0
def grain(self):
    self.play_sound("ding")
    self.pprint(f"곡식 1개를 획득하였습니다.")
    self.player_status[self.game_status.now_turn_player].resource.grain+=1
    
def get_three_resource(self):
    self.play_sound("ding")
    self.pprint(f"갈대, 돌, 밥을 각 1개씩 획득하였습니다.")
    self.player_status[self.game_status.now_turn_player].resource.food+=1
    self.player_status[self.game_status.now_turn_player].resource.reed+=1
    self.player_status[self.game_status.now_turn_player].resource.stone+=1

def FenceConstructionRound(self):
    self.change_main_stacked()
    self.pprint("울타리를 설치해주세요.")
    pass

def Facilities(self):
    pass

def SeedBake(self):
    pass

def FamilyFacility(self):
    pass

def Stone2(self):
    self.play_sound("ding")
    self.pprint(f"돌 {self.random_card_resource["east"][0]}개 획득하였습니다.")
    self.player_status[self.game_status.now_turn_player].resource.stone+=self.random_card_resource["east"][0]
    self.random_card_resource["east"][0] = 0
    pass

def UpgradeFacilities(self):
    pass

def PigMarket(self):
    self.play_sound("pig")
    self.pprint(f"돼지 {self.random_card_resource["pig"][0]}마리를 획득하였습니다.")
    # self.sidebar.btn_sheep_count.setText(str(self.random_card_resource["sheep"][0]))
    self.sidebar.btn_pig_count.setText(f"x{int(self.sidebar.btn_pig_count.text()[1:])+self.random_card_resource["pig"][0]}")
    self.change_main_stacked()
    self.random_card_resource["pig"][0] = 0
    pass

def VegetableSeed(self):
    self.play_sound("ding")
    self.pprint(f"채소종자 1개를 획득하였습니다. 배치하세요.")
    # self.sidebar.btn_sheep_count.setText(str(self.random_card_resource["sheep"][0]))
    self.sidebar.btn_vegetable_count.setText(f"x{int(self.sidebar.btn_vegetable_count.text()[1:])+1}")
    self.change_main_stacked()
    pass

def CowMarket(self):
    self.play_sound("strongcowsound")
    self.pprint(f"소 {self.random_card_resource["cow"][0]}마리를 획득하였습니다.")
    # self.sidebar.btn_sheep_count.setText(str(self.random_card_resource["sheep"][0]))
    self.sidebar.btn_cow_count.setText(f"x{self.random_card_resource["cow"][0]}")
    self.change_main_stacked()
    self.random_card_resource["cow"][0] = 0
    pass

def Stone4(self):
    self.play_sound("ding")
    self.pprint(f"돌 {self.random_card_resource["west"][0]}개 획득하였습니다.")
    self.player_status[self.game_status.now_turn_player].resource.stone+=self.random_card_resource["west"][0]
    self.random_card_resource["west"][0] = 0
    pass

def CultivateSeed(self):
    pass

def HurryFamily(self):
    pass

def UpgradeFence(self):
    pass








from Agricola_Back.Agricola.entity.round_behavior_type import  RoundBehaviorType
def stack_resources(game_status):
    for i in range(14):
        if game_status.round_card_order[i] == RoundBehaviorType.SHEEP1.value:
            game_status.set_round_resource(i, game_status.round_resource[i] + 1)
        if game_status.round_card_order[i] == RoundBehaviorType.COW.value:
            game_status.set_round_resource(i, game_status.round_resource[i] + 1)
        if game_status.round_card_order[i] == RoundBehaviorType.PIG.value:
            game_status.set_round_resource(i, game_status.round_resource[i] + 1)
        if game_status.round_card_order[i] == RoundBehaviorType.STONE_2.value:
            game_status.set_round_resource(i, game_status.round_resource[i] + 1)
        if game_status.round_card_order[i] == RoundBehaviorType.STONE_4.value:
            game_status.set_round_resource(i, game_status.round_resource[i] + 1)
    game_status.set_basic_resource(0, game_status.basic_resource[0] + 1)
    game_status.set_basic_resource(1, game_status.basic_resource[1] + 2)
    game_status.set_basic_resource(2, 1)
    game_status.set_basic_resource(3, game_status.basic_resource[3] + 1)
    game_status.set_basic_resource(4, game_status.basic_resource[4] + 1)
    game_status.set_basic_resource(7, 1)
    game_status.set_basic_resource(10, 2)
    game_status.set_basic_resource(11, game_status.basic_resource[11] + 3)
    game_status.set_basic_resource(12, game_status.basic_resource[12] + 2)
    game_status.set_basic_resource(13, game_status.basic_resource[13] + 1)
    game_status.set_basic_resource(14, game_status.basic_resource[14] + 1)


