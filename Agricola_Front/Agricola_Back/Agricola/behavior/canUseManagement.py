from behavior.job.greengrocer import Greengrocer
from behavior.job.hedger import Hedger
from behavior.job.kiln_baker import KilnBaker
from behavior.job.livestock_dealer import LivestockDealer
from behavior.job.lumberjack import Lumberjack
from behavior.job.magician import Magician
from behavior.job.priest import Priest
from behavior.job.roofer import Roofer
from behavior.job.skilled_bricklayer import SkilledBrickLayer
from behavior.job.small_farmer import SmallFarmer
from behavior.job.sub_cultivator import SubCultivator
from behavior.job.warehouse_manager import WarehouseManager
from behavior.main_facility.dirt_kiln import DirtKiln
from behavior.main_facility.oven1 import Oven1
from behavior.main_facility.oven2 import Oven2
from behavior.main_facility.strong_oven1 import StrongOven1
from behavior.main_facility.strong_oven2 import StrongOven2
from behavior.sub_facility.basket import Basket
from behavior.sub_facility.bottle import Bottle
from behavior.sub_facility.canoe import Canoe
from behavior.sub_facility.giant_farm import GiantFarm
from behavior.sub_facility.grain_shovel import GrainShovel
from behavior.sub_facility.junk_warehouse import JunkWarehouse
from behavior.sub_facility.loam_mining_site import LoamMiningSite
from behavior.sub_facility.manger import Manger
from behavior.sub_facility.pincer import Pincer
from behavior.sub_facility.pitchfork import Pitchfork
from behavior.sub_facility.silpan import SilPan
from behavior.sub_facility.wool_blanket import WoolBlanket
from command import Command


class CanUseManagment(Command):
    def __init__(self):
        self.log_text = None
        self.classes = [Basket,
                        Bottle,
                        Canoe,
                        GiantFarm,
                        GrainShovel,
                        JunkWarehouse,
                        LoamMiningSite,
                        Manger,
                        Pincer,
                        Pitchfork,
                        SilPan,
                        WoolBlanket,
                        Greengrocer,
                        Hedger,
                        KilnBaker,
                        LivestockDealer,
                        Lumberjack,
                        Magician,
                        Priest,
                        Roofer,
                        SkilledBrickLayer,
                        SmallFarmer,
                        SubCultivator,
                        WarehouseManager,
                        DirtKiln,
                        Oven1,
                        Oven2,
                        StrongOven1,
                        StrongOven2]

    def execute(self):
        pass

    def log(self):
        return self.log_text

    def returnCardList(self, input_behavior):
        '''
        input_behavior=현재 행동을 매개변수로 받아옴
        모든 클래스(직업+보조설비+주요설비)에 대해 매개변수로 input_behavior(현재 행동)을 넣어 선언하고
        canuse()를 실행해 현재 사용할수있는 카드들의 리스트를 만들어 반환함
        단 지금 코드는 모든 클래스에 대해 실행하기에 플레이어가 해당 카드를 보유하고있는지는 고려하지않음
        방법 1 - 매개변수로 playerCard로 putjobcard+putfacilitycard를 한 리스트를 받아온후 chk_class_list 대체
        방법 2 - init때 player_status선언후 now_turn_player index로 현재 보유 카드 찾아 chk_class_list 대체
        방법 3 - 리턴받은 곳에서 알아서 플레이어 카드랑 대조
        '''
        chk_class_list = [cls(input_behavior) for cls in self.classes]
        return_class_list = []
        for cls in chk_class_list:
            if (cls.canUse()):
                return_class_list.append(cls)
        return return_class_list