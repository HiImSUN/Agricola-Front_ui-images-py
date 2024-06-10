"""
숙련 벽돌공 직업 카드
"""
from behavior.job.job_interface import JobInterface
from behavior.job.livestock_dealer import LivestockDealer
from behavior.roundbehavior.facilities import Facilities
from behavior.roundbehavior.upgrade_facilities import UpgradeFacilities
from entity import card_type
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


class SkilledBrickLayer(JobInterface):
    def __init__(self, input_behavior):
        self.log_text = None
        self.input_behavior = input_behavior
        self.card_type = card_type.CardType.job
    """
    사용 가능 여부를 반환하는 메소드
    :param:
    :return: 현재 해당 카드 사용 가능 여부
    :rtype: bool
    """
    def canUse(self):
        current_player_cards = player_status_repository.player_status[game_status_repository.game_status.now_turn_player].card.put_job_card
        skilled_brick_layer_card_present = any(isinstance(card, SkilledBrickLayer) for card in current_player_cards)

        if isinstance(self.input_behavior, UpgradeFacilities) or isinstance(self.input_behavior, Facilities) and skilled_brick_layer_card_present:
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
        farm = player_status_repository.player_status[game_status_repository.game_status.now_turn_player].farm
        house_count = farm.get_house_count()
        if house_count >= 3 : # and 흙가마 인 경우:
            player_status_repository.player_status[
                game_status_repository.game_status.now_turn_player].resource.set_brick(
                player_status_repository.player_status[
                    game_status_repository.game_status.now_turn_player].resource.stone + 1
            )
        else:
            pass
        self.log_text = "벽돌공 사용"

    """
    로그 반환
    :param:
    :return: 가장 최근에 저장된 로그 문자열 반환
    :rtype: str
    """
    def log(self):
        pass

    """
    카드 내려놓기 메소드
    :return: 카드 내려놓기 성공 여부 반환
    :rtype: bool
    """
    def putDown(self):
        pass