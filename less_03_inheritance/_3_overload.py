from pprint import pprint


class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calc_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}, {self.salary=}, {self.bonus=}%, total bonus={self.calc_total_bonus()} rub"


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 15)


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, 105000, 40)

    def calc_total_bonus(self):  # перегрузили функцию (переопределили поведение) / синие кружки и стрелочка
        return 200_000


if __name__ == '__main__':
    cleaner = Cleaner("Bob")
    manager = Manager("John")
    ceo = CEO("David")

    print(cleaner)
    print(manager)
    print(ceo)
