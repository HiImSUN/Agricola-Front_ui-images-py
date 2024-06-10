"""
집 한번 고친 후에 울타리 치기 라운드 행동
:param: 플레이어 번호, 바꾸고자 하는 농장 상태
:return: 실행 결과.
:rtype: bool
"""
from behavior.basebehavior.construct_fence import ConstructFence
from behavior.basebehavior.house_upgrade import HouseUpgrade
from behavior.behavior_interface import BehaviorInterface
from behavior.unitbehavior.use_worker import UseWorker
from command import Command
from repository.game_status_repository import game_status_repository
from repository.round_status_repository import round_status_repository


class UpgradeFence(BehaviorInterface):

    def can_play(self):
        return HouseUpgrade().can_play()

    def execute(self):
        return [HouseUpgrade, ConstructFence, UseWorker]

    def log(self):
        pass
