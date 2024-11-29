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


class Iterator:
    def __init__(self, container):
        self.container = container
        self.index = 0

    def __next__(self):
        while 0 <= self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration  # for сам отлавливает и обрабатывает исключение StopIteration, ВСЕ БУДЕТ РАБОТАТЬ


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

    def __len__(self):
        return len(self.container)

    def __call__(self):
        """Ф-я позволяет вызывать объект нашего класса"""
        return f'{sum(e.value for e in self.container)} рублей'

    def __iter__(self):  # цикл for обращается к методу iter за итератором, содержащим метод next
        return Iterator(self.container)  # заменили self на объект класса Iterator

    def __getitem__(self, item: int):  # item либо индекс, либо слово
        if item < 0 or item > len(self.container):
            raise IndexError
        return self.container[item]

    def __setitem__(self, key: int, value: Banknote):  # key либо индекс, либо слово
        if key < 0 or key > len(self.container):
            raise IndexError
        self.container[key] = value


if __name__ == '__main__':
    fifty = Banknote(50)
    hundred = Banknote(100)

    wallet = Wallet(fifty, hundred)
    print(wallet)
    wallet[1] = Banknote(530)  # setitem
    print(wallet)
