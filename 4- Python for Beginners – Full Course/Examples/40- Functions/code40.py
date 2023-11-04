# Functions
# Allows decomposition, readability and reuse

def hello():
    print('Hello!')


hello()  # calling function
hello()  # name should be descriptive
hello()


def hello2(name):
    print('Hello' + name)


hello2("Beau")
hello2("Quincy")


# parameters - values accepted by the function inside function definition
# arguments - values we pass on to these parameters

def hello3(name="my friend!"):
    print('Hello ' + name)


hello3()
hello3("Beau")
hello3("Quincy")


def hello4(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old!")


hello4("Beau", 39)


# parameters are passed by reference, those parameters that are immutable will not
#   be modified outside of function.

def change(value):
    value = 2


val = 1
change(val)
print(val)


# this will not occur if the object is mutable

def change2(value):
    value["name"] = "Syd"


val = {"name": "Beau"}
change2(val)
print(val)


# functions can return values


def hello5(name):
    print("Hello " + name + "!")
    return name


def hello6(name):
    if not name:  # exit function if name is empty
        return
    print("Hello " + name + "!")


hello6(False)
hello6("Breno")


def hello7(name):
    print("Hello " + name + "!")
    return name, "Beau", 8


print(hello7("Syd"))



