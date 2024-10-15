class BlueCat:
    breed = 'Russian Blue'
    names = []
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        BlueCat.increment_count()  # увеличиваем счетчик с кол-вом созданных котов
        self.names.append(name)

    def meow(self):
        print(f"{self.name} of {self.breed} says: Meow!")

    @classmethod
    def increment_count(cls):  # cls is a link to the class
        cls.count += 1

    @classmethod
    def make_cat(cls, name):
        """classmethod часто исп-ся для создания подобных конструкторов(фабрик)"""
        if name == "Tom":
            return cls('Tom', 2)
        elif name == "Musya":
            return cls("Musya", 1)
        return cls("Ginger", 1)

    @staticmethod
    def get_human_age(age):  # cls в этот метод не передается!
        """
        Перевод возраста кошки в возраст человека
        Статикметод не связан напрямую с классом, но мы все равно его инкапсулировали"""
        return age * 8


if __name__ == '__main__':
    tom = BlueCat("Tom", 2)
    musya = BlueCat("Musya", 1)

    print("\n---Pабота self---")
    tom.meow()
    musya.meow()

    print("\n---Pабота staticmethod---")
    print(BlueCat.get_human_age(musya.age))
    print(musya.get_human_age(musya.age))

