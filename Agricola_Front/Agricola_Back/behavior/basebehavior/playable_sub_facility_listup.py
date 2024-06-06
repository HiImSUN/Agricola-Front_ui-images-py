"""
제출 가능한 보조 설비 리스트 업 함수
:param: 플레이어 번호
:return: 제출 가능한 보조 설비 리스트 반환
:rtype: list<card_name>
"""
from command import Command
from repository.player_status_repository import player_status_repository


class PlayableSubFacilityListup(Command):

    def __init__(self, player):
        self.log_text = ""
        self.subFacilityList = self.player_ownCard = player_status_repository.player_status[player].own_card.handSubCard

    def execute(self):
        canUseSubFacilityList = [subFac for subFac in self.subFacilityList if subFac.canPutDown]
        self.log_text = "구매 가능한 보조 설비를 확인했습니다"
        return canUseSubFacilityList

    def log(self):
        return self.log_text
