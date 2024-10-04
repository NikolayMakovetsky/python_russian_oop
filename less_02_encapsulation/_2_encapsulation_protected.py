class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name  # добавили нижнее подчеркивание к атрибутам - подсказка программисту
        self._last_name = last_name
        self._age = age

    def describe(self):
        print(f" I am {self._first_name} {self._last_name}. I'm {self._age} years old!")

if __name__ == '__main__':
    person = Person("Ivan", "Ivanov", 54)
    person._age = 1000  # сработало (нижнее подчеркивание лишь намёк, что так делать не нужно)
    person.age = 2000  # не сработало, защита отработала
    person.describe()