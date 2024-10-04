class Cleaner:
    def __init__(self, name):
        self.name = name
        self.salary = 15000
        self.bonus = 1

    def calc_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f"Cleaner {self.name}, {self.salary=}, {self.bonus=}%, total bonus={self.calc_total_bonus()} rub"


class Manager:
    def __init__(self, name):
        self.name = name
        self.salary = 45000
        self.bonus = 15

    def calc_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f"Manager {self.name}, {self.salary=}, {self.bonus=}%, total bonus={self.calc_total_bonus()} rub"


class CEO:
    def __init__(self, name):
        self.name = name
        self.salary = 105000
        self.bonus = 100

    def calc_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f"CEO {self.name}, {self.salary=}, {self.bonus=}%, total bonus={self.calc_total_bonus()} rub"


if __name__ == '__main__':
    cleaner = Cleaner("Bob")
    manager = Manager("John")
    ceo = CEO("David")

    print(cleaner)
    print(manager)
    print(ceo)
