"""
동물들의 배치 상태가 올바른지 검증하는 로직을 수행하는 클래스.
:param: 3*5 형태의 필드 객체 배열
:return: 배치 상태의 정상 여부를 의미하는 T/F 값.
:rtype: bool
Unit : 종훈
"""
from copy import deepcopy

from command import Command
from entity.field_type import FieldType


class AnimalPositionValidation(Command):
    def __init__(self, field_status):
        self.field_status = deepcopy(field_status)
        self.log_text = None

    def execute(self):
        return self.animal_count_validation()

    def animal_count_validation(self):
        for i, items in enumerate(self.field_status):
            for j, item in enumerate(items):
                if item.field_type == FieldType.CAGE or item.field_type == FieldType.NONE_FIELD:
                    if item.count >= item.maximum:
                        self.log_text = f"({i}, {j})위치에 동물이 너무 많습니다."
                        return False
        return True

    def log(self):
        return self.log_text


"""
1. 울타리 안 or 외양간 안에 있는가 == 최대 제한 수를 넘지 않았는가
    - 울타리 안에 있다 -> 밖부터 순회문 돌리기 -> 순수하게 cage | 외양간 과 cage가 아닌 곳으로
    - 최대 제한 수는 우리를 생성할 때 정의
    - 애초에 존재하면 안되는 밭과 집, 다른 동물이 존재하는 곳 위는 프론트에서 제한하기? -> 프론트의 의사 확인 필요
3. 동물의 종이 전부 같은가
    - 음......
    - 맵 써서 종류 파악하기
    - 빈 값 제외하고 맵 사이즈가 2 이상이면 문제있음
    - 그냥 이건 동물을 옮길 때 검증하자
    


잘못된 입력은 어떻게 받지?
그냥 간단한 "잘못된 곳에는 배치가 안되도록 하는 메소드" 도 필요하다???
ㄴㄴㄴㄴㄴㄴㄴㄴ
잘못된 곳에도 배치가 가능해야, 동물들이 각 칸에 락이 걸렸을 때(교착상태), 위치를 서로 바꿔줄 수 있다.
들판만 가능하게 두고, 다른곳엔 배치 안되게
누르면 증발할텐데? -> 일반 들판도 동물 데이터를 기본적으로 담을 수는 있게?
-> 굳이? -> NoneField 
"""
