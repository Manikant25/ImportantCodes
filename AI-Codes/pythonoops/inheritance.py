
# BASE
class Animal():

    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):

    def __int__(self):
        Animal.__init__(self)
        # Create instance of animal class
        print("Dog Created")

    def who_am_i(self):
        print("I am a Dog")


mydog = Dog()

mydog.eat()

mydog.who_am_i()


# myanimal = Animal()
# myanimal.eat()