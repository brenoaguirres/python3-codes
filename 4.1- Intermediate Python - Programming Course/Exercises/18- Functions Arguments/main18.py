###############################
# FUNCTION ARGUMENTS
###############################

"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args, **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference)
"""


# parameter - function definition // argument - passed to parameters
# positional argument ex:"1" // keyword argument ex:"a=1"
# default arguments can be set in function definition with " test-var='example' "

# variable-length arguments
# *args - used to call any number of positional arguments
# **kwargs - used to call any number of keyword arguments
# can be called other stuff besides *args and **kwargs // ex: *c **d
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo(1, 2, 3, 4, 5, six=6, seven=7)


# forcing keyword arguments with *
def foo2(a, b, *, c, d):  # c and d must be kwargs
    print(a, b, c, d)


foo2(1, 2, c=3, d=4)


# it's possible to unpack a list tuple or dict into args with *
def foo3(a, b, c):
    print(a, b, c)


my_list = [0, 1, 2]
foo3(*my_list)
my_dict = {'a': 'zero', 'b': 'one', 'c': 'two'}  # key names must match
foo3(**my_dict)


# You can access a global var from inside a function but to modify it you'll need the global keyword.
def foo4():
    global number
    x = number
    number = 3
    print("number inside function = ", x)


number = 0
foo4()
print(number)


# call by reference = (python) call by object // call by object reference
# mutable objects like lists or dicts can be changed within a method
# immutable objects like arrays, sets and tuples cannot be changed from a method
# immutable object within a mutable object can be changed within a method
def foo5(a_list):
    a_list += [200, 300, 400]  # appending will not rebind the list


my_list = [1, 2, 3]
foo5(my_list)
print(my_list)


def foo6(a_list):
    a_list = a_list + [200, 300, 400]  # assigning will rebind the list, thus not modifying the global


my_list = [1, 2, 3]
foo6(my_list)
print(my_list)
