
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


class Wallet:

    def __init__(self, *banknotes: Banknote):  # *banknotes = *args
        self.container = []
        self.container.extend(banknotes)

    def __repr__(self):
        return f'Wallet({self.container})'

    def __contains__(self, item):
        """Метод для реализации проверки IN"""
        return item in self.container

    def __bool__(self):
        """Если данный метод не реализован, то питон всегда будет возвращать True
        Проверка на bool для самодельных объектов всегда вернет True, что не всегда верно
        В данном случае, если кошелек пуст, то мы хотим, чтобы возвращался рез-тат False"""
        return len(self.container) > 0

if __name__ == '__main__':
    fifty = Banknote(50)
    hundred = Banknote(100)

    wallet = Wallet(fifty, hundred)
    if wallet:  # __bool__
        print("Wallet has banknotes")
