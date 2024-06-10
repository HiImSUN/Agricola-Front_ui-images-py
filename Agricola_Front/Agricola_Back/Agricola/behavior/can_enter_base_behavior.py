from command import Command
from repository.game_status_repository import game_status_repository
from repository.round_status_repository import round_status_repository


class CanEnterBaseBehavior(Command):
    def __init__(self, behavior_index):
        self.log_text = ""
        self.behavior_index = behavior_index

    def execute(self):
        behavior = game_status_repository.game_status.basic_card_command_factory(self.behavior_index)
        if round_status_repository.round_status.put_basic[self.behavior_index] == -1 and \
                behavior.can_play():
            self.log_text = "행동이 진입가능합니다."
            return True
        else:
            self.log_text = "행동을 진입할 수 없습니다"
            return False

    def log(self):
        return self.log_text
