class Person:
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name  # используем 2 нижних подчеркивания
        self.__last_name = last_name
        self.__age = age
        self.__one__ = 111
        self.__two_ = 222  # некорректное имя атрибута (выдает ошибку при обращении к нему)

    def set_age(self, age):
        if age < 1 or age > 150:
            raise ValueError(f"Age must be in range 1-150")
        self.__age = age

    def describe(self):
        print(f" I am {self.__first_name} {self.__last_name}. I'm {self.__age} years old!")


if __name__ == '__main__':
    person = Person("Ivan", "Ivanov", 54)

    print("\n---Name mangling сработает только если в конце имени атрибута не стоят 2 подчеркивания")
    person._Person__one__ = 1888  # НЕ СРАБОТАЛО
    print(person.__one__)
    person.__one__ = 2888  # СРАБОТАЛО
    print(person.__one__)

    # print(person.__two_)  # AttributeError: 'Person' object has no attribute '__two_'

    print("\n---Private атрибут недоступен, но Name mangling всё равно позволяет получить доступ")
    person.__age = 1000  # НЕ СРАБОТАЛО
    person._age = 2000  # НЕ СРАБОТАЛО
    person.age = 3000  # НЕ СРАБОТАЛО
    person._Person__age = 4000  # СРАБОТАЛО (см. Name mangling)
    person.describe()
