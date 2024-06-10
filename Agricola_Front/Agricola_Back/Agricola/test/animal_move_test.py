import sys, os
from collections import deque
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from command.basebehavior.animal_move_validation import AnimalMoveValidation
from entity.animal_type import AnimalType
from entity.farm.arable_land import ArableLand
from entity.farm.cage import Cage
from entity.farm.none_field import NoneField
from entity.field_type import FieldType
import pytest

class TestAnimalMove:
    # case1: 빈 땅에 동물 옮기기 시도 (가능)
    def test_animal_move_on_nonefield(self):
        # 필드 상태 예시 데이터 (7X11의 일반 땅)
        field_status = [[NoneField() for _ in range(11)] for _ in range(7)]
        # 옮기려는 동물의 위치 설정
        position = (2, 4)  # 3행 5열 위치 (0부터 세어서)
        # 옮기려는 동물 종류 설정
        animal_type = AnimalType.COW  # 예를 들어 소
        # AnimalMoveValidation 인스턴스 생성
        validator = AnimalMoveValidation(field_status, animal_type, position)
        # 실행 메소드 호출
        move_possible = validator.execute()
        assert move_possible == True

    # case2: 빈 우리에 동물 옮기기 시도 (가능)
    def test_animal_move_on_cage(self):
        # 필드 상태 예시 데이터 (7X11의 우리)
        field_status = [[Cage() for _ in range(11)] for _ in range(7)]
        # 옮기려는 동물의 위치 설정
        position = (2, 4)  # 3행 5열 위치 (0부터 세어서)
        # 기존 동물은 없다고 설정
        field_status[5][7].kind = AnimalType.NONE
        # 옮기려는 동물 종류 설정
        animal_type = AnimalType.COW  # 예를 들어 소
        # AnimalMoveValidation 인스턴스 생성
        validator = AnimalMoveValidation(field_status, animal_type, position)
        # 실행 메소드 호출
        move_possible = validator.execute()
        assert move_possible == True

    # case3: 같은 위치에 같은 종류의 동물이 있을 때 옮기기 시도 (가능)
    def test_animal_move_on_same_animal_cage(self):
        # 필드 상태 예시 데이터 (7X11의 우리)
        field_status = [[Cage() for _ in range(11)] for _ in range(7)]
        # 옮기려는 동물의 위치 설정
        position = (2, 4)  # 3행 5열 위치 (0부터 세어서)
        # 기존 동물이 소였다고 설정
        field_status[5][7].kind = AnimalType.COW
        # 옮기려는 동물 종류 설정(기존 동물과 같은 종류로)
        animal_type = AnimalType.COW  # 예를 들어 소
        # AnimalMoveValidation 인스턴스 생성
        validator = AnimalMoveValidation(field_status, animal_type, position)
        # 실행 메소드 호출
        move_possible = validator.execute()
        assert move_possible == True

    # case4: 같은 위치에 다른 종류의 동물이 있을 때 옮기기 시도 (불가능)
    def test_animal_move_on_diff_animal_cage(self):
        # 필드 상태 예시 데이터 (7X11의 우리)
        field_status = [[Cage() for _ in range(11)] for _ in range(7)]
        # 옮기려는 동물의 위치 설정
        position = (2, 4)  # 3행 5열 위치
        # 기존 동물이 돼지였다고 설정
        field_status[5][7].kind = AnimalType.PIG
        # 옮기려는 동물 종류 설정(기존 동물과 다른 종류로)
        animal_type = AnimalType.COW  # 예를 들어 소
        # AnimalMoveValidation 인스턴스 생성
        validator = AnimalMoveValidation(field_status, animal_type, position)
        # 실행 메소드 호출
        move_possible = validator.execute()
        assert move_possible == False

    # case5: 구조물 위에 동물 옮기기 시도 (불가능)
    def test_animal_move_on_structure(self):
        # 필드 상태 예시 데이터 (7X11의 일반 땅)
        field_status = [[NoneField() for _ in range(11)] for _ in range(7)]
        # 옮길 동물 위치 설정
        position = (2, 4)  # 3행 5열 위치
        # 옮길 땅 상태가 구조물(예를 들어 농지)라고 설정
        field_status[5][9] = ArableLand()
        # 옮기려는 동물 종류 설정
        animal_type = AnimalType.COW  # 예를 들어 소
        # AnimalMoveValidation 인스턴스 생성
        validator = AnimalMoveValidation(field_status, animal_type, position)
        # 실행 메소드 호출
        move_possible = validator.execute()
        assert move_possible == False

    # case6: 옆 칸에 다른 동물이 있고 같은 울타리로 둘러싸여 있는 경우 (불가능)
    def test_animal_move_next_diff_animal_unsplited(self):
        # 필드 상태 예시 데이터 (7X11의 우리)
        field_status = [[Cage() for _ in range(11)] for _ in range(7)]
        # 옮기려는 동물의 위치 설정
        position = (2, 4)  # 3행 5열 위치 (0부터 세어서)
        # 옆 칸(3행 4열)에 돼지를 두고
        field_status[5][7].kind = AnimalType.PIG
        # 두 칸 모두 울타리로 가두기
        field_status[5][6].field_type = FieldType.FENCE #상
        field_status[5][10].field_type = FieldType.FENCE #하
        field_status[4][7].field_type = FieldType.FENCE #좌상
        field_status[4][9].field_type = FieldType.FENCE #좌하
        field_status[6][7].field_type = FieldType.FENCE #우상
        field_status[6][9].field_type = FieldType.FENCE #우하
        # 옮기려는 동물 종류 설정
        animal_type = AnimalType.COW  # 예를 들어 소
        # AnimalMoveValidation 인스턴스 생성
        validator = AnimalMoveValidation(field_status, animal_type, position)
        # 실행 메소드 호출
        move_possible = validator.execute()
        assert move_possible == False

    # case7: 옆 칸에 다른 동물이 있지만 울타리로 구분되어 있는 경우 (가능)
    def test_animal_move_next_diff_animal_splited(self):
        # 필드 상태 예시 데이터 (7X11의 우리)
        field_status = [[Cage() for _ in range(11)] for _ in range(7)]
        # 옮기려는 동물의 위치 설정
        position = (2, 4)  # 3행 5열 위치 (0부터 세어서)
        # 옆 칸(3행 4열)에 돼지를 두고
        field_status[5][7].kind = AnimalType.PIG
        # 두 칸 모두 울타리로 가두기
        field_status[5][6].field_type = FieldType.FENCE #상
        field_status[5][10].field_type = FieldType.FENCE #하
        field_status[4][7].field_type = FieldType.FENCE #좌상
        field_status[4][9].field_type = FieldType.FENCE #좌하
        field_status[6][7].field_type = FieldType.FENCE #우상
        field_status[6][9].field_type = FieldType.FENCE #우하
        # 그 두 칸을 구분짓는 울타리 짓기
        field_status[5][8].field_type = FieldType.FENCE #중앙에 울타리 설치
        # 옮기려는 동물 종류 설정
        animal_type = AnimalType.COW  # 예를 들어 소
        # AnimalMoveValidation 인스턴스 생성
        validator = AnimalMoveValidation(field_status, animal_type, position)
        # 실행 메소드 호출
        move_possible = validator.execute()
        assert move_possible == True

# test 실행
if __name__ == "__main__":
    pytest.main()