"""
Python умён
Если нет str, он будет использовать repr

Если не реализованы ни str, ни repr, то будет возвращен адрес объекта в памяти
"""


class Banknote:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):  # для программистов
        """repr должен содержать в себе такую строку, при помощи которой, используя eval,
        можно было бы воссоздать данный объект"""
        return f'Banknote({self.value})'


if __name__ == '__main__':
    banknote = Banknote(10)
    print(banknote)
