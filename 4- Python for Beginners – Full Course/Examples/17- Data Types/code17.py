name = "Breno"  # string
print(type(name))  # return dtype
print(type(name) == str)  # compare dtype
print(isinstance(name, str))  # check if its an instance

age = 2
print(isinstance(age, int))

pi = 3.14
print(isinstance(pi, float))

# python automatically detect dtype
# you can create var from specific type - typecasting

age = float(2)
print(isinstance(age, float))

number = "20"
age = int(number)
print(isinstance(age, int))

# complex for complex numbers
# bool for booleans
# list for lists
# tuple for tuples
# range for ranges
# dict for dictionaries
# set for sets



