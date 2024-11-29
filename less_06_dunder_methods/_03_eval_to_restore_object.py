class Banknote:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):  # для программистов
        return f'Banknote({self.value})'

    def __str__(self):  # для пользователей
        return f'Банкнота номиналом в {self.value} рублей'


if __name__ == '__main__':
    banknote = Banknote(10)
    other = eval(repr(banknote))
    print(banknote, banknote.__class__)
    print(other, other.__class__)
    print(banknote is other)

