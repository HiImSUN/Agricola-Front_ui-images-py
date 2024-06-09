
from gamestate.state import State
from harvest_turn.harvest_change_turn import HarvestChangeTurn
from harvest_turn.harvest_predict_turn_turnstart import HarvestPredictTurnTurnStart
from harvest_turn.harvest_save_undo_point import HarvestSaveUndoPoint
from harvest_turn.harvesting import Harvesting


class HarvestTurnStartState(State):
    def next_state(self):
        self.game_context.set_state(self.game_context.harvest_player_feeding_turn)
        return self.game_context.state.execute()

    def execute(self):
        now_turn = HarvestChangeTurn().execute()
        HarvestPredictTurnTurnStart().execute()
        Harvesting().execute()
        HarvestSaveUndoPoint().execute()
        return f"플레이어 ${now_turn}님, 당신의 수확 턴입니다. 수확 작업을 마무리해주세요."

    def log(self):
        return super().log()
