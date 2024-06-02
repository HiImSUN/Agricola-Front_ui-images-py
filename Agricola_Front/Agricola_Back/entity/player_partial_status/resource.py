"""
건축 자원을 저장하는 엔티티
"""


class Resource:
    def __init__(self):
        self.observers = []
        self.wood = 0
        self.dirt = 0
        self.reed = 0
        self.stone = 0
        self.grain = 0
        self.vegetable = 0
        self.meal = 0
        self.beg_token = 0
        self.first_turn = False

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def set_wood(self, wood):
        self.wood = wood
        self.notify()

    def set_dirt(self, dirt):
        self.dirt = dirt
        self.notify()

    def set_reed(self, reed):
        self.reed = reed
        self.notify()

    def set_rock(self, rock):
        self.rock = rock
        self.notify()

    def set_grain(self, grain):
        self.grain = grain
        self.notify()

    def set_vegetable(self, vegetable):
        self.vegetable = vegetable
        self.notify()

    def set_food(self, food):
        self.food = food
        self.notify()

    def set_beg_token(self, beg_token):
        self.beg_token = beg_token
        self.notify()

    def set_first_turn(self, first_turn):
        self.first_turn = first_turn
        self.notify()