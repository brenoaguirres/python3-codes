# Dictionary: Key-Value Pairs, Unordered, Mutable

# creation
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict = dict(name="Max", age=28, city="New York")
print(mydict)

# accessing values
value = mydict["name"]
print(value)

# adding Key
mydict["email"] = "max@xyz.com"
print(mydict)

# removing Key
del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()  # last inserted item
print(mydict)

# check if key is contained
mydict = {"name": "Max", "age": 28, "city": "New York"}

if "name" in mydict:
    print(mydict["name"])

# looping through
for k in mydict.keys():
    print(k)

for v in mydict.values():
    print(v)

# copying dictionaries
mydict_cpy = mydict  # this will also modify the original, points to the same address
print(mydict_cpy)

mydict_cpy = mydict.copy()  # correct way of doing it, points to different address
mydict_cpy = dict(mydict)

# merging dicts - careful, this will overwrite every kvp that is repeated across the 2 dicts
mydict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
mydict2 = {"name": "Mary", "age": 27, "city": "Boston"}
mydict.update(mydict2)
print(mydict)

# You can use any immutable type as a key
mydict = {3: 9, 6: 36, 9: 81}
print(mydict)
value = mydict[9]
print(value)

mytuple = (8, 7)
mydict = {mytuple: 15}
print(mydict[(8, 7)])

