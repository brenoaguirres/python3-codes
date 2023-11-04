# Generators
# -- Functions that return objects that can be iterated over
# -- Generate the items inside the object lazily (only one at a time and only when you ask for it).
# -- These objects end up being much more memory efficient than other sequence objects.

########################
# Generators
########################

def mygenerator():
    yield 1  # yield instead of return
    yield 2
    yield 3


g = mygenerator()
print(g)

for i in g:
    print(i)

g = mygenerator()
print('\n')

value = next(g)  # will return the first yield value and then pauses at the line
print(value)

value = next(g)  # will continue on the next line
print(value)

# -- a generator object will generate a StopIteration error, if it doesn't find another yield statement
# -- you can use them as input to functions that receive iterables as argument

g = mygenerator()
print('\n')

print(sum(g))  # takes an iterable


g = mygenerator()
print('\n')

print(sorted(g))  # takes an iterable


def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)
value = next(cd)
print(value)
print(next(cd))
print(next(cd))


########################
# Advantages of Generators
########################
# -- very memory efficient

import sys


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


print(sum(firstn(10)))


def firstn_gen(n):
    num = 0
    while num < n:
        yield num
        num +=1


print(sum(firstn_gen(10)))

print(sys.getsizeof(firstn(10000)))  # using getsizeof we can see that this takes much more memory than the gen.
print(sys.getsizeof(firstn_gen(10000)))

########################
# Fibonacci Sequence
########################

# -- common case of use: fibonacci sequence
# -- fib -> first two numbers 0,1 all the following are a sum of the previous two numbers
def fibonacci(limit):
    # 0 1 1 2 3 5 8 13...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(35)
for i in fib:
    print(i)


########################
# Generators Expressions
########################
# written like list comprehensions but with parenthesis instead of square brackets

mygen = (i for i in range(10) if i % 2 == 0)
for i in mygen:
    print(i)

mylist = [i for i in range(10) if i % 2 == 0]
for i in mylist:
    print(i)

print(sys.getsizeof(mylist))  # most expensive
print(sys.getsizeof(mygen))

