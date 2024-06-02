import pytest
from command.basebehavior.fence_validation import FenceValidation
from entity.field_type import FieldType


class TestFenceValidation:
# 내부 비어있음
    def test_fence_validation_success1(self):
        list = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]
        fence_validation = FenceValidation(list)
        list[0][1] = FieldType.FENCE
        list[0][3] = FieldType.FENCE
        list[1][4] = FieldType.FENCE
        list[3][4] = FieldType.FENCE
        list[4][3] = FieldType.FENCE
        list[4][1] = FieldType.FENCE
        list[3][0] = FieldType.FENCE
        list[1][0] = FieldType.FENCE
        assert fence_validation.execute() == True


    # 울타리의 내부에 구조물 존재
    def test_fence_validation_fail1(self):
        list = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]
        list[0][1] = FieldType.FENCE
        list[0][3] = FieldType.FENCE
        list[1][4] = FieldType.FENCE
        list[3][4] = FieldType.FENCE
        list[4][3] = FieldType.FENCE
        list[4][1] = FieldType.FENCE
        list[3][0] = FieldType.FENCE
        list[1][0] = FieldType.FENCE
        list[1][1] = FieldType.HOUSE
        fence_validation = FenceValidation(list)
        assert fence_validation.execute() is False


    # 울타리의 형태가 하나로 이어지지 않음
    def test_fence_validation_fail2(self):
        list = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]
        list[0][1] = FieldType.FENCE
        list[0][3] = FieldType.FENCE
        list[1][4] = FieldType.FENCE
        list[3][4] = FieldType.FENCE
        list[4][3] = FieldType.FENCE
        list[4][1] = FieldType.FENCE
        list[3][0] = FieldType.FENCE
        list[1][0] = FieldType.FENCE
        list[0][9] = FieldType.FENCE
        list[1][10] = FieldType.FENCE
        list[2][9] = FieldType.FENCE
        list[1][8] = FieldType.FENCE
        fence_validation = FenceValidation(list)
        assert fence_validation.execute() is False


    # 울타리의 개수가 15개 이상
    def test_fence_validation_fail3(self):
        list = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]
        list[0][1] = FieldType.FENCE
        list[0][3] = FieldType.FENCE
        list[1][4] = FieldType.FENCE
        list[3][4] = FieldType.FENCE
        list[4][3] = FieldType.FENCE
        list[4][1] = FieldType.FENCE
        list[3][0] = FieldType.FENCE
        list[1][0] = FieldType.FENCE
        list[0][9] = FieldType.FENCE
        list[6][9] = FieldType.FENCE
        list[6][7] = FieldType.FENCE
        list[0][7] = FieldType.FENCE
        list[5][10] = FieldType.FENCE
        list[3][10] = FieldType.FENCE
        list[1][10] = FieldType.FENCE
        list[5][6] = FieldType.FENCE
        list[3][6] = FieldType.FENCE
        list[1][6] = FieldType.FENCE
        list[0][5] = FieldType.FENCE
        list[4][5] = FieldType.FENCE
        fence_validation = FenceValidation(list)
        assert fence_validation.execute() is False


    # 울타리의 형식이 올바르지 않음
    def test_fence_validation_fail4(self):
        list = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]
        list[0][1] = FieldType.FENCE
        list[0][3] = FieldType.FENCE
        list[1][4] = FieldType.FENCE
        list[3][4] = FieldType.FENCE
        list[4][3] = FieldType.FENCE
        list[4][1] = FieldType.FENCE
        list[3][0] = FieldType.FENCE
        list[1][0] = FieldType.FENCE
        list[1][2] = FieldType.FENCE
        fence_validation = FenceValidation(list)
        assert fence_validation.execute() is False
