"""
흙 4개 화덕
"""
from behavior.basebehavior.dump_animal import DumpAnimal
from behavior.main_facility.main_facility_interface import MainFacilityInterface
from entity import card_type
from entity.main_facility_type import MainFacilityType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from entity.animal_type import AnimalType


class StrongOven1(MainFacilityInterface):
    def __init__(self, input_behavior):
        self.log_text = None
        self.input_behavior = input_behavior
        self.card_type = card_type.CardType.main_facility
        self.main_card_type = MainFacilityType.STRONG_OVEN1
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

    def doChange(self, resource_type, resource_value, pos):  # 화로 기능 아무떄나 처리하는 함수 빵굽기는 execute()
        # resource_type => 0 - 채소 1 - 양 2- 돼지 3 - 소
        # resource_value => 굽는 양 ex resource_value=3) 양 3마리 or 돼지 3마리...
        # pos => 해당 동물 위치 / 곡식 바꿀꺼면 None
        if resource_type == 0 and self.player_data.resource.vegetable >= resource_value:
            self.player_data.resource.vegetable -= resource_value
            self.log_text = f"채소 {resource_value}개를 음식 {resource_value * 2}개로 요리했습니다"
            return True

        elif resource_type == 1 and self.player_data.farm.get_sheep_count() >= resource_value:
            if DumpAnimal(AnimalType.SHEEP, pos):
                self.player_data.resource.food += resource_value * 3
                self.log_text = f"양 {resource_value}마리를 음식 {resource_value * 3}개로 요리했습니다"
                return True
            return False

        elif resource_type == 2 and self.player_data.farm.get_pig_count() >= resource_value:
            if DumpAnimal(AnimalType.PIG, pos):
                self.player_data.resource.food += resource_value * 3
                self.log_text = f"돼지 {resource_value}마리를 음식 {resource_value * 3}개로 요리했습니다"
                return True
            return False

        elif resource_type == 3 and self.player_data.farm.get_cow_count() >= resource_value:
            if DumpAnimal(AnimalType.COW, pos):
                self.player_data.resource.food += resource_value * 4
                self.log_text = f"소 {resource_value}마리를 음식 {resource_value * 4}개로 요리했습니다"
                return True
            return False

        else:
            return False

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
        if (any(mainCard.main_card_type in (MainFacilityType.OVEN1, MainFacilityType.OVEN2) for mainCard in
                self.player_data.card.putMainCard)):
            for mainCard in self.player_data.card.putMainCard:
                if mainCard.main_card_type in (MainFacilityType.OVEN1, MainFacilityType.OVEN2):
                    self.player_data.card.putMainCard.remove(mainCard)
                    if (mainCard.main_card_type == MainFacilityType.OVEN1):
                        self.game_status.main_facility_status[
                            1] = -1
                    else:
                        self.game_status.main_facility_status[
                            2] = -1
                    break
        else:
            self.player_data.resource.dirt -= 4
        self.player_data.card.putMainCard.append(self)
        self.game_status.main_facility_status[3] = self.game_status.now_turn_player

    """
    카드 구매 가능 여부를 반환하는 메소드
    :return: 카드 구매 가능 여부 반환
    :rtype: bool
    """

    def canPurchase(self):
        chk_oven = any(mainCard.main_card_type in (MainFacilityType.OVEN1, MainFacilityType.OVEN2) for mainCard in
                       self.player_data.card.putMainCard)
        return (chk_oven or self.player_data.resource.dirt >= 4) and self.game_status.main_facility_status[3] == -1
