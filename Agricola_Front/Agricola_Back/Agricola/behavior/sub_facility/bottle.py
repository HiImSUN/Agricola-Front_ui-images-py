"""
병
"""
from behavior.sub_facility.sub_facility_interface import SubFacilityInterface
from entity import card_type
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


class Bottle(SubFacilityInterface):
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
        # 점수계산때 사용?
        pass

    """
    카드 사용 메소드
    :param: 
    :return: 사용 성공 여부
    :rtype: bool
    """

    def execute(self):
        # 점수계산때 발동?
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
    카드 내려놓기 메소드
    :return: 카드 내려놓기 성공 여부 반환
    :rtype: bool
    """

    def putDown(self):
        current_player = player_status_repository.player_status[game_status_repository.game_status.now_turn_player]
        workers = current_player.worker + current_player.baby
        current_player.card.hand_sub_card.remove(self)
        current_player.card.put_sub_card.append(self)
        current_player.resource.set_dirt(current_player.resource.dirt - workers)
        current_player.resource.set_food(current_player.resource.food - workers)
        self.log_text = "병 카드를 플레이했습니다"
        return True

    """
    카드 내려놓기 가능 여부 반환 메소드
    :return: 카드 내려놓기 가능 여부 반환
    :rtype: bool
    """

    def canPutDown(self):
        current_player = player_status_repository.player_status[game_status_repository.game_status.now_turn_player]
        workers = current_player.worker + current_player.baby
        return current_player.resource.dirt >= workers and current_player.resource.food >= workers
