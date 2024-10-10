"""
Пример из темы Наледование
Мы можем реализовать полиморфную функцию

"""

class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calc_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}, {self.salary=}, {self.bonus=}%, "\
               f"total bonus={self.calc_total_bonus()} rub"


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 15)


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, 105000, 40)

    def calc_total_bonus(self):
        return 200_000


def calc_bonuses(employees: list[Employee]):
    """
    Полиморфная функция
    На вход передается список работников, однако результат будет зависеть от того,
    какие именно работники будут в списке.
    (Работники - представители разных классов/типов)
    """
    for employee in employees:
        print(f"Calc bonus for {employee.name}, it is = {employee.calc_total_bonus()}")

if __name__ == '__main__':
    cleaner = Cleaner("Bob")
    manager = Manager("John")
    ceo = CEO("David")

    print(cleaner)
    print(manager)
    print(ceo)

    a_list = [cleaner, manager, ceo]
    calc_bonuses(a_list)
