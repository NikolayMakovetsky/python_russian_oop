"""namedtuple - первый шаг к ООП"""
from collections import namedtuple

Cat = namedtuple("Cat", 'name age')


def meow():
    print("Meow")


if __name__ == '__main__':
    tom = Cat('Tom', 2)
    print(tom)
    print(tom.name)
    meow()  # метод не привязан к атрибутам именованного кортежа Cat
