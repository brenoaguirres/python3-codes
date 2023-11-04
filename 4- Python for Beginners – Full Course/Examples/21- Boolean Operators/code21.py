condition1 = True
condition2 = False

not condition1  # False
condition1 and condition2  # False
condition1 or condition2  # True

# or - also returns the value of the first operand that is not a False value, otherwise returns the last operand
print(0 or 1)  # 1
print(False or 'hey')  # 'hey'
print('hi' or 'hey')  # 'hi'
print([] or False)  # False
print(False or [])  # []
# other way of thinking
# if x is False then y else x

# and - only evaluates the second argument if the first one is
# if x is False then x else y
print(0 and 1)  # 0
print(1 and 0)  # 0
print(False and 'hey')  # 'False'
print('hi' and 'hey')  # 'hey'
print([] and False)  # []
print(False and [])  # False

# In summary:

# or returns the first truthy value or the last operand if all are falsey.
# and returns the first falsey value or the last operand if all are truthy.
