# Docstrings
# -- documentation for functions, classes
# -- as docstrings follow conventions, they can be processed automatically by IDEs

"""Dog module

This module does ... bla bla bla and provides the
following classes:

- Dog
...
"""

def increment(n):
    """Increment a number"""
    return n + 1


class Dog:
    """A class representing a dog"""
    def __init__(self, name, age):
        """Initialize a dog"""
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""
        print("Woof!")


# built-in fuction to print docstrings
print(help(Dog))

