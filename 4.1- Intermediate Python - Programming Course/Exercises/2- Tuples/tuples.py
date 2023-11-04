# Tuples: ordered, immutable, allows duplicate elements
# -- often used for objects that belongs together
import sys
import timeit

# creation
myTuple = ("Max", 28, "Boston")
print(myTuple)

# even with a single you need a comma to create a tuple
myTuple2 = ("Max",)

# other syntax
myTuple3 = tuple(["Max", 28, "Boston"])  # creating a tuple from an iterable - list
print(myTuple2)
print(myTuple3)

# selecting an item from a tuple
item = myTuple3[0]
item2 = myTuple3[-1]
print(item, item2)

# not possible to modify
# myTuple3[0] = "Tim"

# iterating
for i in myTuple:
    print(i)

# check if contains
if "Max" in myTuple:
    print("Yes")
else:
    print("No")

# checking length, counting items contained, getting index
myTuple = ('a', 'p', 'p', 'l', 'e')
print(len(myTuple))
print(myTuple.count('p'))
print(myTuple.index('p'))  # first appearance

# conversions
myList = list(myTuple)
print(type(myList))
myTuple = tuple(myList)
print(type(myTuple))

# slicing
a = tuple(range(10))
print(a)
b = a[2:5]
print(b)
b = a[::2]
print(b)
b = a[::-1]
print(b)

# unpacking
myTuple = ("Max", 28, "Boston")
name, age, city = myTuple
print(name)
print(age)
print(city)

# unpacking multiple elements with a star
myTuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = myTuple  # i2 will contain a list
print(i1)
print(i2)
print(i3)

# checking efficiency, needs import sys, needs import timeit
myList = [0, 1, 2, "hello", True]
myTuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(myList), "bytes")  # working with a list is more expensive
print(sys.getsizeof(myTuple), "bytes")

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))  # working with a tuple is faster too
# timeit() method calls stmt statement * number variable, number of times.




