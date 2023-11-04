import random

# used to generate pseudo random numbers

########################
# RNG
########################

a = random.random()  # random float in range from 0 to 1
print(a)

a = random.uniform(1, 10)  # random float in range from a to b
print(a)

a = random.randint(1, 10)  # random integer in range from a to b - including b
print(a)

a = random.randrange(1, 10)  # random integer in range from a to b - excluding b
print(a)

a = random.normalvariate(0, 1)  # mu is the mean, sigma is the standard deviation
print(a)

########################
# Functions to work with lists
########################

mylist = list("ABCDEFGH")
print(mylist)
a = random.choice(mylist)  # pick an element
print(a)

a = random.sample(mylist, 3)  # picks a list of k elements, all of them unique
print(a)

a = random.choices(mylist, k=3) # picks a list of k elements, not unique
print(a)

random.shuffle(mylist)  # shuffles a list - modifies in place
print(mylist)

########################
# These numbers are reproducible - pseudo random
########################

random.seed(1)  # will pass a seed, making the reproduction the same every iteration of program

print(random.random())
print(random.randint(1, 10))
print(random.random())
print(random.randint(1, 10))

import datetime
random.seed(int(datetime.datetime.now().timestamp()))  # passing the current time as seed, will return always random

print(random.random())
print(random.randint(1, 10))
print(random.random())
print(random.randint(1, 10))

########################
# These numbers are reproducible - pseudo random
########################
# these pseudonumbers are not recommended to use for security purposes
# for this case is better to use secrets module
# -- used for: passwords, security tokens, account authentication

import secrets

a = secrets.randbelow(10)  # random integer from 0 to n, n not included
print(a)

a = secrets.randbits(4)  # random integer with 4 bits - 1111 max (15)
print(a)

mylist = list((1, 2, 3, 4, 5, 6))
a = secrets.choice(mylist)
print(a)

########################
# Random Arrays
########################
import numpy as np

np.random.seed(random.randrange(100))  # different seed function for np arrays

a = np.random.rand(3)  # 1D array with 3 random floats
print(a)

a = np.random.rand(3, 3)  # 2D array with 3x3 random integers
print(a)

a = np.random.randint(0, 10, (3, 3))  # 3x3 element array with range 0-10 - max excluded
print(a)

np.random.shuffle(a)  # shuffles numpy array - will only shuffle lines, not columns
print(a)




