class BlueCat:
    breed = 'Russian Blue'
    names = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.names.append(name)

    def meow(self):
        print(f"{self.name} of {self.breed} says: Meow!")


if __name__ == '__main__':
    tom = BlueCat("Tom", 2)
    musya = BlueCat("Musya", 1)

    print("\n---Add breed Other for tom---")
    tom.breed = "Other"

    print("\n---Pабота self---")
    tom.meow()
    musya.meow()

    print("\n---Add to class.names extra name Ginger using instance tom---")
    tom.names.append("Ginger")

    print("\n---Print class attribute names using diff instances---")
    print(tom.names)
    print(musya.names)
