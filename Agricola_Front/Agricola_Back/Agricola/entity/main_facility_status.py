"""
주요 설비 카드의 판매 상태 리스트
-1 : 미판매
0 : 1번 플레이어
1 : 2번 플레이어
2 : 3번 플레이어
3 : 4번 플레이어
"""


class MainFacilityStatus:
    def __init__(self):
        self.card_list = [-1 for i in range(5)]
