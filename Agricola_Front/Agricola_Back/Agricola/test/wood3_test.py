# test_wood3.py
import pytest
from command.basicbehavior.wood3 import Wood3
from entity.basic_behavior_type import BasicBehaviorType
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository
from repository.game_status_repository import game_status_repository


class TestWood3:
    @pytest.fixture
    def setup(self):
        # 설정: 플레이어, 게임 상태, 라운드 상태 초기화
        player = 0
        player_status_repository.player_status[player].resource.wood = 0
        game_status_repository.game_status.basic_resource[BasicBehaviorType.WOOD3.value] = 3
        round_status_repository.round_status.put_basic[BasicBehaviorType.WOOD3.value] = False
        return player

    def test_execute_success(self, setup):
        player = setup
        wood3_action = Wood3(player)
        result = wood3_action.execute()
        assert result == True
        assert player_status_repository.player_status[player].resource.wood == 3
        assert wood3_action.log() == "나무 3개를 획득하였습니다."
        assert game_status_repository.game_status.basic_resource[BasicBehaviorType.WOOD3.value] == 0

    def test_execute_already_filled(self, setup):
        player = setup
        round_status_repository.round_status.put_basic[BasicBehaviorType.WOOD3.value] = True
        wood3_action = Wood3(player)
        result = wood3_action.execute()
        assert result == False
        assert player_status_repository.player_status[player].resource.wood == 0
        assert wood3_action.log() == "이번 라운드에 이미 수행된 행동입니다."