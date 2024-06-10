"""
:param: 동물 종류, 동물 수
:return: 제공받은 동물 수가 저장되어 있는 맵
:rtype: 맵(딕셔너리)
동물 획득 과정
    1. 동물 획득 시 획득한 동물 임시 큐로 받기
    2. 그 즉시 프론트에서 해당 동물 큐로 동물 배치 시작하기
    3. 동물 -> 배치하기

    이 커맨드는 획득한 동물을 임시 딕셔너리에 넣어 반환하는 커맨드
"""
from behavior.basebehavior.base_behavior_interface import BaseBehaviorInterface


class GainAnimal(BaseBehaviorInterface):
    def __init__(self, kind, count):
        self.kind = kind
        self.count = count

    def execute(self):
        ret = {self.kind: self.count}
        return ret

    def log(self):
        pass