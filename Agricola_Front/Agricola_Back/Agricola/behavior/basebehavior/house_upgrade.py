"""
집 고치기(업그레이드) 기초 행동
:param: 플레이어 번호
:return: 집 고치기 성공 여부 반환
:rtype: bool
"""
from command import Command
from entity.house_type import HouseType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


class HouseUpgrade(Command):
    def __init__(self):
        player = game_status_repository.game_status.now_turn_player
        self.player_house = player_status_repository.player_status[player].farm.house_status
        self.player_resource = player_status_repository.player_status[player].resource
        self.player_houseNum = player_status_repository.player_status[player].farm.get_house_count()
        self.log_text = ""

    def can_play(self):
        if self.player_house == HouseType.STONE:
            return False
        if ((
                self.player_house == HouseType.WOOD and self.player_resource.dirt >= self.player_houseNum and self.player_resource.reed >= 1)
                or (
                        self.player_house == HouseType.DIRT and self.player_resource.Stone >= self.player_houseNum and self.player_resource.reed >= 1)):
            return True
        return False

    def execute(self):
        if self.player_house == HouseType.WOOD:
            self.player_resource.dirt -= self.player_houseNum
            self.player_resource.reed -= 1
            self.player_house = HouseType.DIRT
            self.log_text = "흙집 업그레이드에 성공했습니다"
            return True
        else:
            self.player_resource.stone -= self.player_houseNum
            self.player_resource.reed -= 1
            self.player_house = HouseType.STONE
            self.log_text = "돌집 업그레이드에 성공했습니다"
            return True

    def log(self):
        return self.log_text
