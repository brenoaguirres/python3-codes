# Modules

# in typical python program, one file acts as the main entry point, and it calls functions
# from other files.

from lib.dog import Dog
import math

roger = Dog("Roger", 5)
roger.walk()
roger.bark()

print(math.sqrt(9))
print(math.pow(8, 2))

# to tell python a folder contains modules, the folder needs an empty file called __init__.py
# highly used modules:
# math for math utilities
# re for regular expressions regex
# json to work with JSON
# datetime to work with dates
# sqlite3 to use SQLite
# os for Operating System utilities
# random for RNG
# statistics for statistics utilities
# requests to perform HTTP network requests
# http to create HTTP servers
# urllib to manage URLs

