"""
울타리 치기 라운드 행동
:param: 플레이어 번호, 변하고자 하는 울타리 상태
:return: 실행 결과.
:rtype: bool
"""
from behavior.basebehavior.construct_fence import ConstructFence
from behavior.behavior_interface import BehaviorInterface
from behavior.unitbehavior.use_worker import UseWorker


class FenceConstructionRound(BehaviorInterface):
    def execute(self):
        return [ConstructFence, UseWorker]

    def log(self):
        pass
