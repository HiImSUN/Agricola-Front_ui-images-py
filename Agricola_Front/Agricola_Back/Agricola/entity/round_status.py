"""
라운드 상태를 저장하는 클래스
"""


class RoundStatus:
    def __init__(self):
        self.observers = []
        self.put_basic = [-1 for i in range(16)]
        self.put_round = [-1 for i in range(14)]
        self.remain_workers = [0, 0, 0, 0]

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def set_put_basic(self, index, value):
        self.put_basic[index] = value
        self.notify()

    def set_put_round(self, index, value):
        self.put_round[index] = value
        self.notify()

    def set_remain_workers(self, index, value):
        self.remain_workers[index] = value
        self.notify()