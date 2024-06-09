from gamestate.state import State
from turn.change_turn import ChangeTurn
from turn.predict_turn_turnstart import PredictTurnTurnStart
from turn.save_undo_point import SaveUndoPoint


class TurnStartState(State):
    def next_state(self):
        self.game_context.set_state(self.game_context.player_turn_state)
        return self.game_context.state.execute()

    def execute(self):
        now_turn_player = ChangeTurn().execute()
        next_turn_player = PredictTurnTurnStart().execute()
        SaveUndoPoint().execute()
        return f"player ${now_turn_player} 의 턴입니다."


    def log(self):
        return super().log()
