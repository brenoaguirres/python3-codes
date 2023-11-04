# Decorators
# -- are a way to change, enhance or alter how a function works
# -- @<decorator_name> before function definition
# -- a decorator is a function that takes a function as a parameter, wraps the function
#       in an inner function that performs something then returns that inner function.

# -- useful when you want to change the behaviour of a function without modifying the function
#       itself.
# -- useful cases: add logging, test performance, perform caching, verify permissions


def logtime(func):
    def wrapper():
        print("before func")
        val = func()
        print("after func")
        return val
    return wrapper


@logtime
def hello():
    print("Hello")


hello()

