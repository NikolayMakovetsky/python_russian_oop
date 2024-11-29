"""
Если мы создаем геттер, но не создаем сеттер, то
установить атрибут НЕВОЗМОЖНО,
Т.О. ОДНА ИЗ НАШИХ ЗАДАЧ УЖЕ РЕШЕНА !!!

НО ПОКА ЕСТЬ И ПРОБЛЕМЫ:
1. ничто не мешает задать ЛЮБОЙ ВОЗРАСТ И ЛЮБОЕ ИМЯ
2. можно присваивать лишние атрибуты
"""

class Cat:
    FIELDS = ('name', 'age')  # !!!

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property  # getter
    def name(self):
        return self._name

    @property  # getter
    def age(self):
        return self._age

    def __repr__(self):
        return f'Cat(name={self.name}, age={self.age})'


if __name__ == '__main__':
    tom = Cat('Tom', 5)
    # tom.name = 100  # AttributeError: property 'name' of 'Cat' object has no setter
    print(tom)
