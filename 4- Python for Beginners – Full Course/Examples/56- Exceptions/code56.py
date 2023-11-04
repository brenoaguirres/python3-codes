# Exceptions

try:
    # some lines of code
    pass
except ZeroDivisionError as errno1:
    # handle this error case
    pass
except ValueError as errno2:
    # handle this error case
    pass
except:
    # handle all other cases
    pass
else:
    # happens if there are no exceptions
    pass
finally:
    # happens whether there are or not any exceptions
    pass

# other exceptions
# EOFError - End of file
# TypeError - incorrect type

try:
    result = 2 / 0
except ZeroDivisionError as e:
    print('Cannot divide by zero!')
finally:
    result = -1

print(result)

# You can raise exceptions on purpose using raise statement
try:
    raise Exception('An error!')
except Exception as error:
    print(error)


# Create custom exceptions
class DogNotFoundException(Exception):
    print("inside")
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog Not Found!')