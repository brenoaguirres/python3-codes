# Objects
# -- Everything in python are objects - int, float, lists, tuples

age = 8
# age has now access to the properties and methods defined to all int objects
print(age.real)
print(age.imag)

print(age.bit_length())

items = [1, 2]
items.append(3)
items.pop()
print(id(items))  # we can see memory location of object

# some objects are mutable, others immutable
print(id(age))
age = age + 1  # this will be a new object
print(id(age))


