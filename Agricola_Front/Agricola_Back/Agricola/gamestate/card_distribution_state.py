from gameready.card_distribution import CardDistribution
from gamestate.state import State


class CardDistributionState(State):
    def next_state(self):
        self.game_context.set_state(self.game_context.round_start_state)
        return self.game_context.state.execute()

    def execute(self):
        CardDistribution().execute()
        return "카드 분배가 완료되었습니다. 각자의 카드를 확인해주세요."

    def log(self):
        return super().log()
