"""
카드 분배 커맨드
각 player_status 의 card 객체에 6장의 카드 번호를 넣는다.
"""
import random

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
from entity.sub_facility_type import sub_facility_type_reverse_map
from repository.player_status_repository import player_status_repository


class CardDistribution(Command):

    def execute(self):
        sub_card_list = random.sample(range(12), 12)
        for i in range(4):
            for j in range(3):
                if sub_card_list[i * 3 + j] == 0:
                    player_status_repository.player_status[i].card.handSubCard.append( \
                        Basket())
                if sub_card_list[i * 3 + j] == 1:
                    player_status_repository.player_status[i].card.handSubCard.append( \
                        Bottle())
                if sub_card_list[i * 3 + j] == 2:
                    player_status_repository.player_status[i].card.handSubCard.append( \
                        Canoe())
                if sub_card_list[i * 3 + j] == 3:
                    player_status_repository.player_status[i].card.handSubCard.append( \
                        GiantFarm())
                if sub_card_list[i * 3 + j] == 4:
                    player_status_repository.player_status[i].card.handSubCard.append( \
                        GrainShovel())
                if sub_card_list[i * 3 + j] == 5:
                    player_status_repository.player_status[i].card.handSubCard.append( \
                        JunkWarehouse())
                if sub_card_list[i * 3 + j] == 6:
                    player_status_repository.player_status[i].card.handSubCard.append( \
                        LoamMiningSite())
                if sub_card_list[i * 3 + j] == 7:
                    player_status_repository.player_status[i].card.handSubCard.append( \
                        Manger())
                if sub_card_list[i * 3 + j] == 8:
                    player_status_repository.player_status[i].card.handSubCard.append( \
                        Pincer())
                if sub_card_list[i * 3 + j] == 9:
                    player_status_repository.player_status[i].card.handSubCard.append( \
                        Pitchfork())
                if sub_card_list[i * 3 + j] == 10:
                    player_status_repository.player_status[i].card.handSubCard.append( \
                        SilPan())
                if sub_card_list[i * 3 + j] == 11:
                    player_status_repository.player_status[i].card.handSubCard.append( \
                        WoolBlanket())


        job_card_list = random.sample(range(12), 12)
        for i in range(4):
            for j in range(3):
                if job_card_list[i * 3 + j] == 0:
                    player_status_repository.player_status[i].card.handJobCard.append( \
                        Greengrocer())
                if job_card_list[i * 3 + j] == 1:
                    player_status_repository.player_status[i].card.handJobCard.append( \
                        Hedger())
                if job_card_list[i * 3 + j] == 2:
                    player_status_repository.player_status[i].card.handJobCard.append( \
                        KilnBaker())
                if job_card_list[i * 3 + j] == 3:
                    player_status_repository.player_status[i].card.handJobCard.append( \
                        LivestockDealer())
                if job_card_list[i * 3 + j] == 4:
                    player_status_repository.player_status[i].card.handJobCard.append( \
                        Lumberjack())
                if job_card_list[i * 3 + j] == 5:
                    player_status_repository.player_status[i].card.handJobCard.append( \
                        Magician())
                if job_card_list[i * 3 + j] == 6:
                    player_status_repository.player_status[i].card.handJobCard.append( \
                        Priest())
                if job_card_list[i * 3 + j] == 7:
                    player_status_repository.player_status[i].card.handJobCard.append( \
                        Roofer())
                if job_card_list[i * 3 + j] == 8:
                    player_status_repository.player_status[i].card.handJobCard.append( \
                        SkilledBrickLayer())
                if job_card_list[i * 3 + j] == 9:
                    player_status_repository.player_status[i].card.handJobCard.append( \
                        SmallFarmer())
                if job_card_list[i * 3 + j] == 10:
                    player_status_repository.player_status[i].card.handJobCard.append( \
                        SubCultivator())
                if job_card_list[i * 3 + j] == 11:
                    player_status_repository.player_status[i].card.handJobCard.append( \
                        WarehouseManager())
    def log(self):
        pass
