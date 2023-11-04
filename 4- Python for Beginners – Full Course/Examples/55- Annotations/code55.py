# Annotations
# -- python is dinamically typed
# -- annotations allow us to optionally type stuff
# -- this way we can show what type we're expecting for different values

# -- python will ignore these annotations, some IDEs treat that, otherwise you'll have to
#       use a standalone tool called mypi


# without annotations
# def increment(n):
#     return n + 1

# with annotations
def increment(n: int) -> int:  # receives an int and returns an int, respectively
    return n + 1



count: int = 0

