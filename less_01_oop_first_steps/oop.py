class Cat:
    def __init__(self, name, age):
        """Инизиализация - передача данных в экземпляр при его создании"""
        self.name = name
        self.age = age

    def meow(self):
        print(self)  # self - неявный атрибут содержащий ссылку на экземпляр класса
        print(f"{self.name} says: Meow!")



if __name__ == '__main__':
    tom = Cat("Tom", 2)
    musya = Cat("Musya", 1)

    print("\n---Объект класса---")
    print(tom is musya)  # False
    print(type(tom))  # <class '__main__.Cat'>
    print(musya)  # <__main__.Cat object at 0x000001F6FDDBC0D0>

    print("\n---Pабота self---")
    tom.meow()
    Cat.meow(tom)  # именно так происходит под капотом в строке: tom.meow()
