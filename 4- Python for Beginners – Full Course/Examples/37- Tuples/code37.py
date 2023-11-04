# tuples are immutable
names = ("Roger", "Syd", "Barry")
print(names[0])
names.index("Roger")
print(names[-1])

# len()
print(len(names))

# in operator
print("Roger" in names)

# slicing
print(names[0:1])

# sorted - creates a new tuple
print(sorted(names))
print(names)

# + operator
newTuple = names + ("Tina", "Quincy")
print(newTuple)

