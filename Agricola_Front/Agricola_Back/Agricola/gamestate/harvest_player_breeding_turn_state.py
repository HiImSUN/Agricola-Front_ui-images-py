from gamestate.state import State
from harvest_turn.feeding_family import FeedingFamily


class HarvestPlayerBreedingTurnState(State):
    def next_state(self):
        self.game_context.set_state(self.game_context.harvest_turn_end_state)
        return self.game_context.state.execute()

    def execute(self):
        beg = FeedingFamily().execute()
        return f"구걸 토큰 ${beg} 개 획득."

    def log(self):
        return super().log()
