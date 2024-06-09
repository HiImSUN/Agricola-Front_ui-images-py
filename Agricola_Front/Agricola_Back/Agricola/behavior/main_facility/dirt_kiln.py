"""
흙가마
"""
from behavior.main_facility.main_facility_interface import MainFacilityInterface
from entity import card_type
from entity.main_facility_type import MainFacilityType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


class DirtKiln(MainFacilityInterface):
    def __init__(self, input_behavior):
        self.log_text = None
        self.input_behavior = input_behavior
        self.card_type = card_type.CardType.main_facility
        self.main_card_type = MainFacilityType.DIRT_KILN
        self.game_status = game_status_repository.game_status
        self.player_data = player_status_repository.player_status[
            game_status_repository.game_status.now_turn_player]

    """
    사용 가능 여부를 반환하는 메소드
    :param:
    :return: 현재 해당 카드 사용 가능 여부
    :rtype: bool
    """

    def canUse(self):
        pass

    """
    카드 사용 메소드
    :param: 
    :return: 사용 성공 여부
    :rtype: bool
    """

    def execute(self):
        pass

    """
    로그 반환
    :param:
    :return: 가장 최근에 저장된 로그 문자열 반환
    :rtype: str
    """

    def log(self):
        return self.log_text

    """
    카드 구매 메소드
    :return: 카드 구매 성공 여부 반환
    :rtype: bool
    """

    def purchase(self):
        self.player_data.resource.set_dirt(self.player_data.resource.dirt - 3)
        self.player_data.resource.set_stone(self.player_data.resource.stone - 1)
        self.player_data.card.putMainCard.append(self)
        self.game_status.main_facility_status[0] = self.game_status.now_turn_player
        if self.player_data.resource.grain != 0: self.execute()

    """
    카드 구매 가능 여부를 반환하는 메소드
    :return: 카드 구매 가능 여부 반환
    :rtype: bool
    """

    def canPurchase(self):
        return self.player_data.resource.dirt >= 3 and self.player_data.resource.stone >= 1 and  self.game_status.main_facility_status[0] == -1
