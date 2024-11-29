"""
Если не реализован метод eq, питон считает равными объекты
при условии что это один и тот же объект
"""


class Banknote:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):  # для программистов
        return f'Banknote({self.value})'

    def __str__(self):  # для пользователей
        return f'Банкнота номиналом в {self.value} рублей'

    def __eq__(self, other):
        """Обязательно проверяй тип входящего объекта"""
        if other is None or not isinstance(other, Banknote):  # важное условие, чтобы избежать ошибки
            return False
        return self.value == other.value

    def __ne__(self, other):
        """Обязательно проверяй тип входящего объекта"""
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value != other.value

    def __lt__(self, other):
        """Обязательно проверяй тип входящего объекта"""
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value < other.value

    def __le__(self, other):
        """Обязательно проверяй тип входящего объекта"""
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value <= other.value

    def __gt__(self, other):
        """Обязательно проверяй тип входящего объекта"""
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value > other.value

    def __ge__(self, other):
        """Обязательно проверяй тип входящего объекта"""
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value >= other.value


if __name__ == '__main__':
    fifty = Banknote(50)
    hundred = Banknote(100)

    print(fifty == hundred)  # F
    print(fifty != hundred)  # T
    print(fifty > hundred)  # F
    print(fifty < hundred)  # T
    print(fifty >= hundred)  # F
    print(fifty <= hundred)  # T

