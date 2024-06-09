from gamestate.state import State
from round.SetRoundWorkerResource import SetRoundWorkerResource
from round.open_new_round_card import OpenNewRoundCard
from round.predict_turn_roundstart import PredictTurnRoundStart
from round.stack_resources import StackResources


class RoundStartState(State):
    def next_state(self):
        self.game_context.set_state(self.game_context.turn_start)
        return self.game_context.state.execute()

    def execute(self):
        card = OpenNewRoundCard().execute()
        StackResources().execute()
        PredictTurnRoundStart().execute()
        SetRoundWorkerResource().execute()
        return f"새 카드가 공개되었습니다. 공개된 카드 : ${card}"


    def log(self):
        return super().log()

