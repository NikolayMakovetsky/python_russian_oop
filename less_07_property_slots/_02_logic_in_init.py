class Cat:

    def __init__(self, name, age):
        """Проблема такого подхода в том, что можно
        создать правильного кота, а потом изменить
        атрибуты на некорректные, и ошибки не будет"""
        if not name:
            raise AttributeError("Name can't be empty!")
        if age > 15 or age < 1:
            raise AttributeError("Age should be in 1-15")
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat(name={self.name}, age={self.age})'


if __name__ == '__main__':
    tom = Cat('Tom', 2)
    print(tom)
    tom.age = 99
    print(tom)
    # bars = Cat('', 2)  # AttributeError: Name can't be empty!
    # tusya = Cat(name='Tusya', age=17)  # AttributeError: Age should be in 1-15
