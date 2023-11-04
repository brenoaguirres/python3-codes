# enums - readable names bound to a constant value
from enum import Enum


class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])
# this is the only way to create constants in python

# list the values for the Enum
print(list(State))

# count the total values for the Enum
print(len(State))
