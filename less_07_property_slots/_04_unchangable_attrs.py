
class Cat:

    FIELDS = ('name', 'age')  # !!!

    def __init__(self, name, age):
        self.name = name  # setattr
        self.age = age  # setattr

    def __repr__(self):
        return f'Cat(name={self.name}, age={self.age})'

    def __setattr__(self, key, value):
        if key not in self.FIELDS:
            raise AttributeError(f"Only allowed {self.FIELDS}") # !!!
        if key == 'name' and not value:
            raise AttributeError("Name can't be empty!")
        if key == 'age' and (value > 15 or value < 1):
            raise AttributeError("Age should be in 1-15")
        self.__dict__[key] = value



if __name__ == '__main__':
    # tom = Cat('Tom', 50)  # AttributeError: Age should be in 1-15
    # tom.age = 99  # AttributeError: Age should be in 1-15
    # tom = Cat('', 10)  # AttributeError: Name can't be empty!
    tom = Cat('Tom', 5)
    print(tom)
    # tom.age2 = 99 AttributeError: Only allowed ('name', 'age')


