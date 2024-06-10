"""
곡식 활용 라운드 행동
빈 밭만큼 곡식 선택하고, 해당 곡식을 심는다
그리고 빵 굽기 여부를 통해 빵 굽기를 수행한다.
:param: 플레이어 번호, 빵 굽기 여부, 선택한 밭과 곡물
:return: 실행 결과.
:rtype: bool
"""
from behavior.basebehavior.do_bake import DoBake
from behavior.behavior_interface import BehaviorInterface
from behavior.unitbehavior.use_worker import UseWorker
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from behavior.basebehavior.seed_plant import SeedPlant


# Todo

class SeedBake(BehaviorInterface):

    def __init__(self,game_status,player_status,round_status):
        self.log_text = ""

    def can_play(self):
        return True

    def execute(self):
        ret = [SeedPlant]
        if player_status_repository.player_status[game_status_repository.game_status.now_turn_player].card.put_main_card:
            ret.append(DoBake)
        ret.append(UseWorker)
        return ret
    def log(self):
        return self.log_text
