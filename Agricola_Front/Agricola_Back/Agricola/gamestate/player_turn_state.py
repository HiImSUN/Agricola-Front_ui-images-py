from gamestate.state import State


class PlayerTurnState(State):
    def next_state(self):
        self.game_context.set_state(self.game_context.turn_end_state)
        return self.game_context.state.execute()

    def execute(self):
        return "턴이 시작되었습니다."

    def log(self):
        return super().log()
