"""
돌 집게
"""
from behavior.sub_facility.sub_facility_interface import SubFacilityInterface
from entity import card_type
from behavior.roundbehavior.stone_2 import Stone2
from behavior.roundbehavior.stone_4 import Stone4
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


class Pincer(SubFacilityInterface):
    def __init__(self, input_behavior):
        self.log_text = None
        self.input_behavior = input_behavior
        self.card_type = card_type.CardType.sub_facility

    """
    사용 가능 여부를 반환하는 메소드
    :param:
    :return: 현재 해당 카드 사용 가능 여부
    :rtype: bool
    """

    def canUse(self):
        current_player_cards = player_status_repository.player_status[
            game_status_repository.game_status.now_turn_player].card.put_sub_card
        pincer_card_present = any(isinstance(card, Pincer) for card in current_player_cards)

        if (isinstance(self.input_behavior, Stone2) or isinstance(self.input_behavior,
                                                                  Stone4)) and pincer_card_present:
            return True
        else:
            return False

    """
    카드 사용 메소드
    :param: 
    :return: 사용 성공 여부
    :rtype: bool
    """

    def execute(self):
        player_status_repository.player_status[
            game_status_repository.game_status.now_turn_player].resource.set_stone(
            player_status_repository.player_status[
                game_status_repository.game_status.now_turn_player].resource.stone + 1
        )
        self.log_text = "돌 집게 효과로 돌 하나를 추가로 얻습니다"
        return True

    """
    로그 반환
    :param:
    :return: 가장 최근에 저장된 로그 문자열 반환
    :rtype: str
    """

    def log(self):
        return self.log_text

    """
    카드 내려놓기 메소드
    :return: 카드 내려놓기 성공 여부 반환
    :rtype: bool
    """

    def putDown(self):
        current_player = player_status_repository.player_status[game_status_repository.game_status.now_turn_player]
        current_player.resource.set_wood(current_player.resource.wood - 1)
        current_player.card.hand_sub_card.remove(self)
        current_player.card.put_sub_card.append(self)
        self.log_text = "돌 집게 카드를 플레이했습니다"
        return True

    """
    카드 내려놓기 가능 여부 반환 메소드
    :return: 카드 내려놓기 가능 여부 반환
    :rtype: bool
    """

    def canPutDown(self):
        return player_status_repository.player_status[
            game_status_repository.game_status.now_turn_player].resource.wood >= 1
