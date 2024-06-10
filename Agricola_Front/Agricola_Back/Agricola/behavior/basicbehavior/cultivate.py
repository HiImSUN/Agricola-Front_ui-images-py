"""
밭 일구기 기본 행동
:param: 플레이어 번호, 변하고자 하는 밭 상태 # 플레이어 번호 날림 by jy

:return: 실행 결과.
:rtype: bool
"""
from behavior.behavior_interface import BehaviorInterface
from behavior.basebehavior.arable_expansion import ArableExpansion
from behavior.unitbehavior.use_worker import UseWorker


class Cultivate(BehaviorInterface):

    def __init__(self):
        self.log_text = ""

    def execute(self):
        return [ArableExpansion, UseWorker]


    def log(self):
        return self.log_text
