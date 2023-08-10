class Animal:
    """Animal class, all animals will inherit this class"""
    def __int__(self, name):
        self.name = name


class Cat(Animal):

    def __int__(self, name):
        super().__int__(name)

    def make_sound(self):
        print(f'${self.name} says Meow')
        return


class Dog(Animal):
    def __int__(self, name):
        super().__int__(name)

    def make_sound(self):
        print(f'${self.name} says Woof')
        return


cat = Cat("kitty")
cat.make_sound()

dog = Dog("jack")
dog.make_sound()
