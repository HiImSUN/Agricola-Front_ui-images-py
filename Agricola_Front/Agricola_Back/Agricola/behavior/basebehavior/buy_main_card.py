"""
카드 구매하는 함수
인자로 구매하고 싶은 카드를 받아온다
살 수 있는지 검증하고
살 수 있으면 자원을 깎고 플레이어의 put_main_card 에 추가한다
살 수 없으면 False 를 반환한다.
"""
from behavior.basebehavior.base_behavior_interface import BaseBehaviorInterface


class BuyMainCard(BaseBehaviorInterface):
    def __init__(self, want_to_buy):
        self.want_to_buy = want_to_buy
        self.log_text = ""

    def log(self):
        return self.log_text

    def execute(self):
        want = self.want_to_buy(None)
        if want.canPurchase():
            want.purchase()
            self.log_text = want.log()
            return True
        else:
            self.log_text = want.log()
            return False

