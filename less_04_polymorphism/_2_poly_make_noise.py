"""
В языках со статической типизацией полиморфизм реализуется именно так,
то есть НА ОСНОВЕ ТИПА
Компилятор или интерпретатор смотрит КЕМ ЯВЛЯЕТСЯ тот, у которого мы хотим вызвать действие,
и на основе этого вызывает соответствующий метод
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


def noise(animal: Animal):
    animal.make_noise()


if __name__ == '__main__':
    noise(Cat())
    noise(Dog())
