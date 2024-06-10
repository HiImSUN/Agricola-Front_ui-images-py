from gamestate.state import State
from harvest_turn.check_harvest_turn_remain import CheckHarvestTurnRemain
from repository.game_status_repository import game_status_repository


class HarvestTurnEndState(State):
    def next_state(self):
        if game_status_repository.game_status.next_turn_player == -1:
            self.game_context.set_state(self.game_context.round_end_state)
        else:
            self.game_context.set_state(self.game_context.harvest_turn_start_state)
        return self.game_context.state.execute()

    def execute(self):
        CheckHarvestTurnRemain().execute()
        return "남은 플레이어가 있는지 검사중입니다. 계속하려면 확인 버튼을 클릭해주세요."

