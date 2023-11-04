# dictionaries work with KVPs (Key Value Pairs)
dog = {"name": "Roger", "age": 8, "fur": "yellow"}
print(dog["name"])
print(dog['age'])

dog['name'] = "Syd"
print(dog)

# other way of getting element
print(dog.get("name"))
print(dog.get("color"))  # will return None
print(dog.get("color", "brown"))  # if it can't find color key, then will return brown by default

# pop
print(dog.pop("name"))
print(dog)

# popitem - will remove the last item
print(dog.popitem())
print(dog)

# check if key is contained
print("color" in dog)
print("age" in dog)

# get list of keys
print(dog.keys())  # will get dict keys
print(list(dog.keys()))  # will get just the keys

# get list of values
print(dog.values())  # will get dict values
print(list(dog.values()))  # will get just the values

# get all items
print(list(dog.items()))

# length
print(len(dog))

# adding pairs
dog["favorite food"] = "Meat"
print(dog)

# delete kvp
del dog["age"]
print(dog)

# copy dict
dogCopy = dog.copy()
dogCopy["color"] = "yellow"
print(dog)
print(dogCopy)



