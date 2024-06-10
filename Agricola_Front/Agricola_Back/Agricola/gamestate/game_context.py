"""
게임 진행 파사드

게임 현재 진행 상태 파악 -> 엔티티
엔티티를 보고 게임 상태 변경
다음 상태가 무엇인지를 파악하는 로직 작성이 여기서 이루어진다

게임 진행 버튼(게임 시작, 턴 종료 등) 버튼을 눌렀을 때 순서대로 수행되어야 하는 행동

상태 패턴의 적용 필요성?

0라운드
    1. 카드 분배
    2. 초기 자원 분배
0->1라운드
    1. 게임판 치우기
    2. 새 라운드 카드 공개하기
    3. 자원 쌓기
    
턴 시작
    1. 남은 일꾼 수 체크
    2. 턴 전환 스택 초기화
    3. Undo checkpoint 저장
턴 종료
    1. now player 전환
    2. next player 변경
턴 건너뛰기
    1. now player 전환
    2. next player 변경
4->5라운드
    1. 수확 시작
    2. 수확 종료
    3. 게임판 치우기
    4. 새 라운드 카드 공개하기
    5. 자원 쌓기
수확 턴 진입
    1. undo checkpoint 저장
    2. 농장 단계 처리
    3. 가족 먹여살리기 진입
    4. 번식 단계 -> 동물 배치
    5. 턴 종료
수확 시작
    1. 수확 인터페이스로 변경
    2. 플레이어 1, 2, 3, 4 차례로 수확 턴 진입 함수 호출
수확 종료
    2. 수확 인터페이스에서 기존 인터페이스로 돌아오기
동물 배치는?
    1. 동물 획득 시 동물 큐로 받기
    2. 그 즉시 프론트에서 해당 동물 큐로 동물 배치 시작하기
    3. 큐에 동물 넣어두고 하나씩 프론트에서 정보 받기 -> 배치하기
"""
from gamestate.game_end_state import GameEndState
from gamestate.game_start_state import GameStartState
from gamestate.harvest_player_breeding_turn_state import HarvestPlayerBreedingTurnState
from gamestate.harvest_player_feeding_turn_state import HarvestPlayerFeedingTurnState
from gamestate.harvest_start_state import HarvestStartState
from gamestate.harvest_turn_end_state import HarvestTurnEndState
from gamestate.harvest_turn_start_state import HarvestTurnStartState
from gamestate.player_turn_state import PlayerTurnState
from gamestate.card_distribution_state import CardDistributionState
from gamestate.round_end_state import RoundEndState
from gamestate.round_start_state import RoundStartState
from gamestate.state import State
from gamestate.turn_end_state import TurnEndState
from gamestate.turn_start_state import TurnStartState


class GameContext:
    def __init__(self):
        self.game_start_state = GameStartState(self)
        self.game_end_state = GameEndState(self)
        self.card_distribution_state = CardDistributionState(self)
        self.harvest_start_state = HarvestStartState(self)
        self.harvest_player_feeding_turn_state = HarvestPlayerFeedingTurnState(self)
        self.harvest_player_breeding_turn_state = HarvestPlayerBreedingTurnState(self)
        self.harvest_turn_start_state = HarvestTurnStartState(self)
        self.harvest_turn_end_state = HarvestTurnEndState(self)
        self.round_start_state = RoundStartState(self)
        self.round_end_state = RoundEndState(self)
        self.turn_start_state = TurnStartState(self)
        self.turn_end_state = TurnEndState(self)
        self.player_turn_state = PlayerTurnState(self)
        self.state: State = self.game_start_state

    def set_state(self, state):
        self.state = state

    def next_state(self):
        return self.state.next_state()


game_context = GameContext()