########################
# ASTERISK OPERATOR
########################

result = 5 * 2  # multiplication
result = 5 ** 2  # power
result = [0, 1] * 10  # list with 10 '0', '1' // [0, 1, 0, 1, 0, 1 ...
#                     # also works with strings


# *args **kwargs
# def foo(a, b, *args, **kwargs):  # any number of args and kwargs
# def foo(a, b, *, c, d):  # force c d being kwargs
# def foo(*args, a, b, c, d):  # force all args being kwargs

# argument unpacking
# my_list = [0, 1, 2]
# foo(*my_list)

# dict unpacking - kw must match function
# my_dict = {'a': 0, 'b': 1}
# foo(**my_dict)

# unpacking multiple items to list
numbers = (0, 1, 2, 3, 4, 5, 6)
*beginning, last = numbers
print(beginning)  # will always get the remaining unpacked elements
print(last)

beginning, second, *last = numbers
print(beginning)
print(second)
print(last)  # always returns a list, even numbers being a tuple

beginning, *middle, last = numbers
print(middle)


# merge iterables to list
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
new_list = [*my_tuple, *my_list]


