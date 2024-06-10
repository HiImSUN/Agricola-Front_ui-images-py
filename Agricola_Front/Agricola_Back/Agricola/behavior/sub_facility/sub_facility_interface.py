"""
보조 설비 카드 행동 인터페이스
"""
from abc import abstractmethod

from command import Command


class SubFacilityInterface(Command):
    """
    카드 사용 메소드
    :param:
    :return: 사용 성공 여부
    :rtype: bool
    """
    @abstractmethod
    def execute(self):
        pass

    """
    로그 반환
    :param:
    :return: 가장 최근에 저장된 로그 문자열 반환
    :rtype: str
    """
    @abstractmethod
    def log(self):
        pass

    """
    카드 내려놓기 메소드
    :return: 카드 내려놓기 성공 여부 반환
    :rtype: bool
    """
    @abstractmethod
    def putDown(self):
        pass

    """
    카드 내려놓기 가능 여부 반환 메소드
    :return: 카드 내려놓기 가능 여부 반환
    :rtype: bool
    """
    @abstractmethod
    def canPutDown(self):
        pass

    """
    사용 가능 여부를 반환하는 메소드
    :param:
    :return: 현재 해당 카드 사용 가능 여부
    :rtype: bool
    """
    @abstractmethod
    def canUse(self):
        pass