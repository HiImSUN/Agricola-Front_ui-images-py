from entity.game_status import GameStatus
from gamestate.state import State
from repository.game_status_repository import game_status_repository
from round.baby_handling import BabyHandling
from round.clean_game_board import CleanGameBoard
from round.round_change import RoundChange


class RoundEndState(State):
    def next_state(self):
        if game_status_repository.game_status.now_round == 14:
            self.game_context.set_state(self.game_context.game_end_state)
        else:
            self.game_context.set_state(self.game_context.round_start_state)
        return self.game_context.state.execute()

    def execute(self):
        BabyHandling().execute()
        CleanGameBoard().execute()
        RoundChange().execute()
        return "라운드가 종료되었습니다. 게임판을 정리합니다."


    def log(self):
        return super().log()
