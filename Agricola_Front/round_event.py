# from Agricola_Back.Agricola.behavior.roundbehavior.sheep_market import SheepMarket
def SheepMarket(self):
    sheep_card_index = self.game_status.get_sheep_card_index()
    self.pprint(f"양 {self.random_card_resource["sheep"][0]}마리를 획득하였습니다.")
    # self.sidebar.btn_sheep_count.setText(str(self.random_card_resource["sheep"][0]))
    self.sidebar.btn_sheep_count.setText(f"x{int(self.sidebar.btn_sheep_count.text()[1:])+self.random_card_resource["sheep"][0]}")
    self.change_main_stacked()
    self.random_card_resource["sheep"][0] = 0

    # ret = [PlaceAnimal,GainAnimal(AnimalType.SHEEP, self.game_status.round_resource[sheep_card_index]), UseWorker]
def FenceConstructionRound(self):
    pass

def Facilities(self):
    pass

def SeedBake(self):
    pass

def FamilyFacility(self):
    pass

def Stone2(self):
    pass

def UpgradeFacilities(self):
    pass

def PigMarket(self):
    pass

def VegetableSeed(self):
    pass

def CowMarket(self):
    pass

def Stone4(self):
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


