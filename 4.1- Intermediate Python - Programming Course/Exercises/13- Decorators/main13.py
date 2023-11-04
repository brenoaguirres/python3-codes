# Decorators
# -- 2 types - Function & Class decorators
# -- a decorator is a function that takes another function as an argument and modify its behaviour without
#       explicitly modifying it
# -- functions in python are first class objects - they can be defined inside a function, passed as an argument
#       to another function and even returne from a function.

########################
# Decorators
########################

def start_end_decorator(func):

    def wrapper():
        # do before func
        print('Start')
        func()
        # do after func
        print('End')
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

# print_name = start_end_decorator(print_name)  # how decorator works BTS


print_name()


########################
# *args , **kwargs
########################
# -- use args, kwargs in the start_end_decorator's wrapper so it can take as many arguments as needed
# -- return result inside wrapper so it can return the value to outside

def start_end_decorator2(func):

    def wrapper(*args, **kwargs):
        # do before func
        print('Start')
        result = func(*args, **kwargs)
        # do after func
        print('End')
        return result
    return wrapper

@start_end_decorator2
def add5(x):
    return x + 5


result = add5(10)
print(result)


########################
# Function Identity
########################


import functools

print(help(add5))
print(add5.__name__)  # python got confused with name of function
# so lets use @functools.wraps to correct __name__


def start_end_decorator3(func):

    @functools.wraps(func)  # preserves information of used function (func)
    def wrapper(*args, **kwargs):
        # do before func
        print('Start')
        result = func(*args, **kwargs)
        # do after func
        print('End')
        return result
    return wrapper


@start_end_decorator3
def add10(x):
    return x + 10


print(help(add10))
print(add10.__name__)  # python got confused with name of function


########################
# Decorator with arguments, Inner function with inner function
########################

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name='Breno'):
    print(f'Hello {name}')


greet()


########################
# Nested Decorators
########################

def new_startend_dec(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper


def debug(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug
@new_startend_dec
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting


say_hello("Breno")


########################
# Class Decorator
########################
# -- do the same as decorators but are tipically used if we want to maintain and update a state
#   ex: keep track of how many times i've executed this function


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):  # can use the object of this class as a function to call
        self.num_calls += 1
        print(f'This was executed {self.num_calls} times')
        return self.func(*args, **kwargs)


# cc = CountCalls(None)  # creating and calling obj as function via call method
# cc()

@CountCalls
def say_hello2():
    print('Hello')


say_hello2()
say_hello2()
say_hello2()


########################
# Useful Cases
########################
# -- implement a timer decorator to calculate time of a function
# -- debug decorator to print info about the code function and its arguments
# -- check if the arguments will fill some requirements and adapt the behaviour accordingly
# -- register functions - like plugins - with decorators
# -- cache the return values
# -- add info or update the state


