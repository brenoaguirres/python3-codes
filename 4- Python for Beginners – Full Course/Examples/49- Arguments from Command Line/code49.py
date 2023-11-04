# Arguments CLI

import sys

# run prog from CLI:
# python main.py

# use sys module to pass arguments via CLI:
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    quit()

print(sys.argv)  # will print name of file + arguments passed
print("Hello " + str(name))


