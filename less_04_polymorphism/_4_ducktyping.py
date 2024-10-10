"""
Ducktyping - утиная типизация
Этот термин получил распространение после статьи Алекса Мортелли,
где он написал, что если что-то ходит как утка и крякает как утка,
то мы считаем что это утка, независимо от того, является ли объект
уткой на самом деле
"""


class Animal:
    def make_noise(self):
        print("Shh")


class Cat(Animal):
    def make_noise(self):
        print("Meow")


class Dog(Animal):
    def make_noise(self):
        print("Gavv")


class Car:
    def make_noise(self):
        print("Bi-bi")


def noise(animal: Animal):
    """ Ducktyping in Python
    Благодаря этому принципу мы можем передать в функцию аргумент-объект любого типа,
    НО главное, чтобы у этого объекта был реализован метод make_noise()
    """
    animal.make_noise()


if __name__ == '__main__':
    noise(Cat())
    noise(Dog())
    noise(Car())  # PyCharm подчеркивает строчку благодаря аннотации noise(animal: Animal)
    # Однако с т.з. питона никакой ошибки нет! Концепция Ducktyping в действии.
