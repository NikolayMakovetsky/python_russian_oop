"""
HAS-A принцип ООП ("СОДЕРЖИТ")
Это важный принцип в КОМПОЗИЦИИ

(Машина содержит и колесо, и двигатель)

"""


class Engine:
    def start(self):
        pass


class Wheel:
    pass


class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = [Wheel()] * 4

    def turn_key(self):
        self.engine.start()


if __name__ == '__main__':
    pass
