class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe(self):
        print(f" I am {self.first_name} {self.last_name}. I'm {self.age} years old!")

if __name__ == '__main__':
    person = Person("Ivan", "Ivanov", 54)
    person.age = 1000  #  Хотелось бы защитить экземпляр от подобного рода вмешательств
    person.describe()