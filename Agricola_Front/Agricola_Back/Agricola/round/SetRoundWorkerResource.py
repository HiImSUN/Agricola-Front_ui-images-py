from command import Command
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository


class SetRoundWorkerResource(Command):
    def execute(self):
        round_status = round_status_repository.round_status
        for i in range(4):
            round_status.set_remain_workers(i, player_status_repository.player_status[i].worker)

    def log(self):
        return "일꾼이 할당되었습니다."