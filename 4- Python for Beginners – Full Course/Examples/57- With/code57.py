# With statement
# -- help working with exception handling
# -- When working with files, the process is simplified

filename = 'C:\\Users\\breno.aguirres\\Desktop\\Code\\4- Python for Beginners – Full Course\\Examples\\57- With\\text.txt'

with open(filename, 'r') as file:
    # close will be called automatically
    content = file.read()
    print(content)




