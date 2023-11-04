##########################
# SHALLOW VS DEEP COPYING
##########################


# assignment copies the reference, it won't make an actual copy
# not a problem for immutable types, but it is a problem for mutable types
org = 5
cpy = org
cpy = 6  # will not affect original - immutable
print(org)
print(cpy)

org = [0, 1, 2, 3]
cpy = org
cpy[1] = 79  # will affect original - mutable
print(org)
print(cpy)

# shallow copy: one level deep, only references of nested child objects
# deep copy: fully independent copy
import copy
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)  # will make shallow copy
cpy[1] = 79
print(org)
print(cpy)

# shallow copy - won't work for nested lists
# x = copy.copy(y)
# x = y.copy()
# x = list(y)
# x = y[:]

# deep copy - work with nested lists (matrices)
org = [[0, 1, 2, 3], [4, 5, 6, 7]]
cpy = copy.deepcopy(org)  # will make fully independent copy
cpy[0][1] = 79
print(org)
print(cpy)

# this copy methods will work for instances of objects too
# for nested classes, also it's better to use deepcopy()
