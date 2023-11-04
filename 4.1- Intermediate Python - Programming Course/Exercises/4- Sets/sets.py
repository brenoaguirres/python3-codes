# Sets: unordered, mutable, no duplicates

# creating sets
myset = {1, 2, 3, 1, 2}  # not allowed duplicates
print(myset)

myset = set("Hello")  # not allowed duplicates, order is arbitrary
print(myset)  # this is also a trick to find how many different chars are in your word

myset = set()  # an empty set should be called this way, if you use {}, you create a dict

# adding, removing items to set
myset = {1, 2, 3, 1, 2}
myset.add(4)
myset.add(5)
print(myset)

myset.remove(4)
myset.remove(5)
print(myset)

myset.discard(4)  # discard will remove item if found, but ignore if not found -- will not generate an error
print(myset)

# empty set
value = myset.pop()  # return arbitrary value and removes it
myset.clear()  # clear set
print(value, myset)

# iterate over
myset = {1, 2, 3, 4, 5}
for i in myset:
    print(i)

# checking if its contained
if 1 in myset:
    print("Yes")
else:
    print("No")

# union and intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

uni = odds.union(evens)  # will combine both sets without repetition
print(uni)
inter = odds.intersection(primes)  # gets elements found in both sets
print(inter)

# difference - returns all elements from first set that are not in the second set
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
diff = setA.difference(setB)
print(diff)

diff = setA.symmetric_difference(setB)  # returns all elements from both sets that aren't on the other
print(diff)

# update - updates by adding different elements found in another set
setA.update(setB)
print(setA)

setA.intersection_update(setB)  # updates by keeping only elements found in both sets
print(setA)

setA.difference_update(setB)  # updates by removing elements found in another set
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.symmetric_difference_update(setB)
print(setA)


# superset, subset, disjoint
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3}
setC = {10, 11, 12}

print(setA.issuperset(setB))
print(setB.issubset(setA))
print(setA.isdisjoint(setC))  # True if both have a null intersection

# careful copying sets, because they're mutable
# copying sets

setA = {1, 2, 3, 4, 5, 6}
setB = setA  # wrong

setB = setA.copy()
setB = set(setA)

# frozen set
# immutable version of normal set
lista = [1, 2, 3, 4]
fset = frozenset(lista)
print(type(fset))
print(fset)
# can't add, remove, pop, etc. from frozensets

