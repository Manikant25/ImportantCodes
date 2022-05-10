mylist = [1, 2, 3, 4]

myset = set()


# print(type(myset))


class Dog():
    #  CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS

    species = 'mammal'

    def __init__(self, mybreed, name, spots):
        # Attribute
        # We assign it using self.attribute_name
        self.my_attribute = mybreed
        self.name = name
        self.spots = spots

    def myFuctions(self):
        print(self.my_attribute)
        print(self.name)
        print(self.spots)
        print(self.species)

    #  OPERATIONS / ACTIONS - - - - > Method
    def bark(self, number):
        print("WOOF ! My name is {} and the number is {}".format(self.name, number))


my_dog = Dog("LAB", "Bluezo", True)

print(type(my_dog))
# print(my_dog.breed)
my_dog.species = "Bird"
my_dog.myFuctions()

my_dog.bark(10)


class Circle():
    pi = 3.14

    def __init__(self, radius=10):
        self.radi = radius
        self.area = self.radi * self.radi

    #     Method
    def getCircumference(self):
        return 2 * self.pi * self.radi



circle = Circle()

print(circle.getCircumference())
print(circle.pi)
print(circle.radi)

cirle2 = Circle(20)
print(cirle2.radi)
print(cirle2.getCircumference())
print(cirle2.area)
