"""
ЗАЧЕМ БЫЛ ПРИДУМАН SLOTS?

Проблема в том, что даже объект класса Cat, всего с 2-мя полями
занимает приблизительно 350 байт (если измерить при помощи pympler.asizeof())
А ЭТО МНОГО !

SLOTS ЗАМЕНЯЕТ __dict__ на КОРТЕЖ !!!
Основная цель слотс - уменьшить память, которую занимает объект
Поэтому объект класса Cat теперь занимает не 350, а 135 байт !!!
Плюс SLOTS жестко определяем имена допустимых для объекта атрибутов
"""


class Cat:
    #  Теперь в наш объект нельзя добавить новые атрибуты
    __slots__ = ('_name', '_age')  # slots - заменитель FIELDS

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
    # tom.name2 = 'Tomas'  # AttributeError: 'Cat' object has no attribute 'name2'
    print(tom)

