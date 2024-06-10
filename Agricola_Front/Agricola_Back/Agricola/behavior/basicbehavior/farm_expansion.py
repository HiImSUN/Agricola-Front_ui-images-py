"""
농장 확장 기본 행동
:param: 플레이어 번호, 변하고자 하는 필드 상태
:return: 실행 결과.
:rtype: bool
"""
from behavior.basebehavior.construct_barn import ConstructBarn
from behavior.behavior_interface import BehaviorInterface
from behavior.basebehavior.house_expansion import HouseExpansion
from behavior.unitbehavior.use_worker import UseWorker


class FarmExpansion(BehaviorInterface):

    def __init__(self):
        self.log_text = ""

    def can_play(self):
        # 농장 확장이 가능한 위치가 있는지 확인
        return True

    def execute(self):
        return [HouseExpansion, ConstructBarn, UseWorker]

    def log(self):
        return self.log_text
