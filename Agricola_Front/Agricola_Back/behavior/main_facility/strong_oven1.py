"""
흙 4개 화덕
"""
from behavior.main_facility.main_facility_interface import MainFacilityInterface


class StrongOven1(MainFacilityInterface):
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
        pass

    """
    카드 구매 메소드
    :return: 카드 구매 성공 여부 반환
    :rtype: bool
    """
    def purchase(self):
        pass