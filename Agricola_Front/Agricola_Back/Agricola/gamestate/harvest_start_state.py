from gamestate.state import State
from harvest.harvest_predict_turn_roundstart import HarvestPredictTurnRoundStart


class HarvestStartState(State):
    def next_state(self):
        self.game_context.state.set_state(self.game_context.harvest_turn_state)
        return self.game_context.state.execute()

    def execute(self):
        HarvestPredictTurnRoundStart().execute()
        return "수확 라운드가 시작되었습니다. 모두 수확을 준비해주세요."

    def log(self):
        return super().log()
