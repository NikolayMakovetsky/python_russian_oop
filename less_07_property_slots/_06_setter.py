"""
Если мы создаем геттер, но не создаем сеттер, то
установить атрибут НЕВОЗМОЖНО,
Т.О. ОДНА ИЗ НАШИХ ЗАДАЧ УЖЕ РЕШЕНА !!!

НО ПОКА ЕСТЬ И ПРОБЛЕМЫ:
1. ничто не мешает задать ЛЮБОЙ ВОЗРАСТ И ЛЮБОЕ ИМЯ (смотри ниже)
2. можно присваивать лишние атрибуты (смотри файлы _07_, _08_)

ВАЖНО!
Когда нет сеттера (@age.setter)
то нам в конструкторе класса приходится писать ЧЕРЕЗ НИЖНЕЕ ПОДЧЕРКИВАНИЕ,
НО КОГДА МЫ НАПИСАЛИ СЕТТЕР, ТО ЭТИ ПОДЧЕРКИВАНИЯ ДЛЯ КОРРЕКТНОЙ РАБОТЫ НУЖНО УБРАТЬ
X - self._name = name
V - self.name = name
self._name, self._age будут создаваться внутри сеттеров !!!
"""


class Cat:
    FIELDS = ('name', 'age')  # !!!

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property  # getter
    def name(self):
        return self._name

    @name.setter  # setter
    def name(self, value):
        if not value:
            raise AttributeError("Name can't be empty!")
        self._name = value

    @property  # getter
    def age(self):
        return self._age

    @age.setter  # setter
    def age(self, value):
        if value > 15 or value < 1:
            raise AttributeError("Age should be in 1-15")
        self._age = value

    def __repr__(self):
        return f'Cat(name={self.name}, age={self.age})'


if __name__ == '__main__':
    tom = Cat('Tom', 5)
    tom.name = 'Tomas'  # setter
    tom.age = 10  # setter
    print(tom)

    # angela = Cat('Angela', 111)  # прокатит, если в init: self._age = age
    # print(angela)
