# map(), filter(), reduce()

# map()
# -- used to run a function upon each item in an iterable
# -- create a list with the same number of items, but their values
#       can be changed
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# when a function is one-liner like this, it's common to map as a lambda function
# def double(a):
#    return a * 2
# double = lambda a: a * 2
# but instead of assigning to double, let's just assign directly to map function

result = map(lambda a: a * 2, numbers)  # runs double for each item in numbers
print(list(result))


# filter()
# -- takes an iterable and returns a filter object
# -- which is another iterable but without some of the original items
# -- you can do so, by returning True or False from the filtering function

numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda n: n % 2 == 0, numbers)
print(list(result))


# reduce()
# -- used to calculate a value out of a sequence
# -- have to be imported from functools
expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]

sum = 0
for expense in expenses:
    sum += expense[1]

print(sum)

# quicker way of doing the calculation with reduce
# -- first argument is accumulated value
# -- second argument is the updating value
sum = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum)

