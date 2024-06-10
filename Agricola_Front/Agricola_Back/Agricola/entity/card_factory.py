from behavior.basicbehavior.cultivate import Cultivate
from behavior.basicbehavior.daily_labor import DailyLabor
from behavior.basicbehavior.dirt1 import Dirt1
from behavior.basicbehavior.dirt2 import Dirt2
from behavior.basicbehavior.farm_expansion import FarmExpansion
from behavior.basicbehavior.fishing import Fishing
from behavior.basicbehavior.meeting_place import MeetingPlace
from behavior.basicbehavior.reed import Reed
from behavior.basicbehavior.resource_market import ResourceMarket
from behavior.basicbehavior.seed import Seed
from behavior.basicbehavior.side_job1 import SideJob1
from behavior.basicbehavior.side_job2 import SideJob2
from behavior.basicbehavior.theater import Theater
from behavior.basicbehavior.wood1 import Wood1
from behavior.basicbehavior.wood2 import Wood2
from behavior.basicbehavior.wood3 import Wood3
from behavior.roundbehavior.cow_market import CowMarket
from behavior.roundbehavior.cultivate_seed import CultivateSeed
from behavior.roundbehavior.facilities import Facilities
from behavior.roundbehavior.family_facility import FamilyFacility
from behavior.roundbehavior.fence_construction_round import FenceConstructionRound
from behavior.roundbehavior.hurry_family import HurryFamily
from behavior.roundbehavior.pig_market import PigMarket
from behavior.roundbehavior.seed_bake import SeedBake
from behavior.roundbehavior.sheep_market import SheepMarket
from behavior.roundbehavior.stone_2 import Stone2
from behavior.roundbehavior.stone_4 import Stone4
from behavior.roundbehavior.upgrade_facilities import UpgradeFacilities
from behavior.roundbehavior.upgrade_fence import UpgradeFence
from behavior.roundbehavior.vegetable_seed import VegetableSeed


def basic_card_command_factory(self, basic_index):
    if basic_index == 0:
        return Wood1
    if basic_index == 1:
        return Wood2
    if basic_index == 2:
        return ResourceMarket
    if basic_index == 3:
        return Dirt1
    if basic_index == 4:
        return Theater
    if basic_index == 5:
        return FarmExpansion
    if basic_index == 6:
        return MeetingPlace
    if basic_index == 7:
        return Seed
    if basic_index == 8:
        return Cultivate
    if basic_index == 9:
        return SideJob1
    if basic_index == 10:
        return DailyLabor
    if basic_index == 11:
        return Wood3
    if basic_index == 12:
        return Dirt2
    if basic_index == 13:
        return Reed
    if basic_index == 14:
        return Fishing
    if basic_index == 15:
        return SideJob2


def round_card_command_factory(self, round_index):
    if self.round_card_order[round_index] == 0:
        return SheepMarket
    if self.round_card_order[round_index] == 1:
        return FenceConstructionRound
    if self.round_card_order[round_index] == 2:
        return Facilities
    if self.round_card_order[round_index] == 3:
        return SeedBake
    if self.round_card_order[round_index] == 4:
        return FamilyFacility
    if self.round_card_order[round_index] == 5:
        return Stone2
    if self.round_card_order[round_index] == 6:
        return UpgradeFacilities
    if self.round_card_order[round_index] == 7:
        return PigMarket
    if self.round_card_order[round_index] == 8:
        return VegetableSeed
    if self.round_card_order[round_index] == 9:
        return CowMarket
    if self.round_card_order[round_index] == 10:
        return Stone4
    if self.round_card_order[round_index] == 11:
        return CultivateSeed
    if self.round_card_order[round_index] == 12:
        return HurryFamily
    if self.round_card_order[round_index] == 13:
        return UpgradeFence