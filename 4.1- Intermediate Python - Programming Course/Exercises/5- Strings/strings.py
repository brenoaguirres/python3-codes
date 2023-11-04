# Strings - ordered, immutable, text representation

# creating a string
my_string = "Hello World"
print(my_string)

# careful with escaping characters
my_string = 'I\'m a programmer!'
print(my_string)

# multiline strings
my_string = """Hello 
World"""
print(my_string)

# To not create a new line in multiline
my_string = """Hello \
World"""
print(my_string)

# Getting char from string
my_string = "Hello World"
char = my_string[-1]
print(char)
# not possible - strings are immutable -> my_string[0] = 'F'

# substrings
my_string = "Hello World"
substring = my_string[:5]  # from beginning
print(substring)
substring = my_string[::-1]  # reverse
print(substring)
substring = my_string[:]  # entire
print(substring)
substring = my_string[3:7]  # last exclusive
print(substring)

# concatenation
stringA = "Tom and "
stringB = "Jerry"
sentence = stringA + stringB
print(sentence)

# iterate over
sentence = "Hello"
for i in sentence:
    print(i)

# check if contains
if 'H' in sentence:
    print("Yes")

# methods
my_string = '         Hello World          '
print(my_string)
my_string = my_string.strip()  # removes whitespaces
print(my_string)

print(my_string.upper())
print(my_string.lower())
print(my_string.startswith('H'))
print(my_string.endswith('World'))

print(my_string.find('o'))  # index of the appearance of substring
print(my_string.count('l'))
print(my_string.replace('World', 'Universe'))

# split e join

my_string = "how are you doing"
my_list = my_string.split()
print(my_list)
my_string = " ".join(my_list)
print(my_string)

my_string = "8,7,5,6"
my_list = my_string.split(",")
print(my_list)

# multiplying strings
my_list = ['a'] * 6
print(my_list)
my_string = " ".join(my_list)
print(my_string)

from timeit import default_timer as timer
start = timer()
stop = timer()
print(stop-start)

# formatting strings
# %, .format(), f-strings
var = 3.14159265
my_string = "The variable is %.2f" % var  # %s %d %h %.2f
print(my_string)

my_string = "The variable is {:.2f}".format(var)
print(my_string)

my_string = f"The variable is {var:.2f}"
print(my_string)
