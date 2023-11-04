# Classes
# Obj is an instance of a class, class is the type of obj

class Animal:
    def walk(self):
        print("Walking...")


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")


roger = Dog("Roger", 8)
roger.bark()
print(roger.name)
print(type(roger))

roger.walk()
roger.walk()
roger.bark()

