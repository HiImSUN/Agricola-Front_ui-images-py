from gamestate.state import State


class HarvestPlayerFeedingTurnState(State):
    def next_state(self):
        self.game_context.set_state(self.game_context.harvest_player_breeding_turn_state)
        return self.game_context.state.execute()

    def execute(self):
        return "주의 : 턴 종료 버튼 클릭 시, 현재 상태로 가족 급식을 진행합니다."