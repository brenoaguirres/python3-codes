# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = list()
print(mylist2)

# Allows different dtypes
mylist2 = [5, True, "apple", "apple"]
print(mylist2)

# Access by index
item = mylist[0]
print(item)
item = mylist2[2]
print(item)
item = mylist[-1]
print(item)

# Iterate over list
for i in mylist:
    print(i)

# Check if is within list
if "banana" in mylist:
    print("yes")
else:
    print("no")

# check how many elements
print(len(mylist))

# append items
mylist.append("lemon")
print(mylist)

# inserting at specific index
mylist.insert(2, "blueberry")
print(mylist)

# removing items
print(mylist.pop())  # returns and removes last item
print(mylist)

# remove at specific element
mylist.remove("cherry")  # if specified unexisting element will generate ValueError
print(mylist)

# clear list
print(mylist.clear())

mylist = ["apple", "banana", "blueberry", "cherry", "lemon"]

# reverse list
print(mylist)
mylist.reverse()
print(mylist)

# sort list
mylist = [-4, 3, 1, -1, -5, 10]
print(mylist)
mylist.sort()  # don't return list, change list value
print(mylist)

# sort list without change its value
mylist = [-4, 3, 1, -1, -5, 10]
print(mylist)
new_list = sorted(mylist)
print(new_list)

# list operations
mylist = [0] * 5
print(mylist)

mylist2 = [1, 2, 3, 4, 5]
new_list = mylist + mylist2
print(new_list)

# slicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]  # last exclusive
print(a)

a = mylist[:4]
print(a)

a = mylist[4:]
print(a)

a = mylist[:]
print(a)

a = mylist[::2]
print(a)

a = mylist[::-1]
print(a)

# copying a list
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org
print(list_cpy)
list_cpy.pop()  # will also modify the original list
print(list_org)

# use .copy() instead to make an actual copy or list() function or slicing
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org.copy()
print(list_cpy)

list_org = ["banana", "cherry", "apple"]
list_cpy = list(list_org)
print(list_cpy)

list_org = ["banana", "cherry", "apple"]
list_cpy = list_org[:]
print(list_cpy)

# list comprehension - elegant way to create a new list from existing one with 1 line
mylist = [1, 2, 3, 4, 5, 6]
mylist2 = [i*i for i in mylist]  # will create a list of squares based on list a
print(mylist2)
# the syntax consists in ["expression, for item in list"]

