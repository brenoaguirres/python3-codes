# Lambda Functions // anonymous functions
# -- tiny functions that have no name
# -- lambda argument : expression
# -- must have a single expression
# -- has to return a value (must be an expression, not a statement)

# -- they cannot be invoked directly but can be assigned to variables
# --

multiply2 = lambda num: num * 2

multiply = lambda a, b: a * b

print(multiply(2, 4))
print(multiply2(7))

# -- their utilities comes when combined with other python functionalities like:
#       map, filter, reduce

