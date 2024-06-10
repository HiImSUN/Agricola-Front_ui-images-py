from gameready.round_card_shuffle import RoundCardShuffle
from gameready.start_resource_distribution import StartResourceDistribution
from gamestate.state import State


class GameStartState(State):
    def __init__(self, game_context):
        super().__init__(game_context)
        StartResourceDistribution().execute()
        RoundCardShuffle().execute()

    def next_state(self):
        self.game_context.set_state(self.game_context.card_distribution_state)
        return self.game_context.state.execute()

    def execute(self):
        pass

    def log(self):
        return super().log()



