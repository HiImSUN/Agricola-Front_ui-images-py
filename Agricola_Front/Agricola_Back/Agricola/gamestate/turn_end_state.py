from gamestate.state import State
from repository.game_status_repository import game_status_repository
from turn.check_turn_remain import CheckTurnRemain


class TurnEndState(State):
    def next_state(self):
        if game_status_repository.next_turn_player == -1:
            if game_status_repository.now_round in [3, 6, 8, 10, 12, 13]:
                self.game_context.set_state(self.game_context.harvest_start_state)
            else:
                self.game_context.set_state(self.game_context.round_end_state)
        else:
            self.game_context.set_state(self.game_context.turn_start_state)
        return self.game_context.state.execute()

    def execute(self):
        CheckTurnRemain().execute()
        return "남은 플레이어가 있는지 검사중입니다. 계속하려면 확인 버튼을 클릭해주세요."

    def log(self):
        return super().log()
