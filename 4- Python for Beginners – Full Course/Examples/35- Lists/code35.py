dogs = ["Roger", 1, "Syd", True, "Quincy", 7]

print("Roger" in dogs)
print("Beau" in dogs)

cats = []  # empty list

print(dogs[0])
print(dogs[-1])
print(dogs[2])

dogs[2] = "Aguirres"
print(dogs)

print(dogs[-2])

# slicing
print(dogs[2:4])
print(dogs[2:])
print(dogs[:4])
print(dogs[::2])

# length
print(len(dogs))

# append
dogs.append("Judah")
print(len(dogs))
print(dogs)

# extend
dogs.extend(["Judah", 5, "Ronaldo"])
print(dogs)

# +=
dogs += ["F", 5, "Parker"]
print(dogs)
dogs += "James"  # this one will add each letter as an element
print(dogs)

# remove items
dogs.remove("Aguirres")
print(dogs)
print(dogs.pop())
print(dogs)

# insert items
items = ["Roger", "Syd", "Quincy"]
items.insert(2, "James")
print(items)

items[1:1] = ["Benjamin", "Frank"]
print(items)



