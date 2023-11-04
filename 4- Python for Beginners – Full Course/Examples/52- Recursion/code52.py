# Recursion
# -- a recursive function will always have a base case, and a recursive case
# -- a recursive function will call itself inside the function
# -- the base case is when we are going to stop the function
# -- without the base case, it will run forever and return a RecursionError

def factorial(n):
    if n == 1: return 1
    return n * factorial(n - 1)


print(factorial(5))

