from gameover.rank_calculate import RankCalculate
from gameover.score_calculation import ScoreCalculation
from gamestate.state import State


class GameEndState(State):
    def next_state(self):
        exit()

    def execute(self):
        ScoreCalculation().execute()
        result = RankCalculate().execute()
        return result

    def log(self):
        return super().log()
