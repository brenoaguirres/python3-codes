##############################
# CONTEXT MANAGERS
##############################

# Context managers allow to allocate and release resources precisely
# with statement


# we use this instead of the second way, which isn't much as cleaner as this
with open('notes.txt', 'w') as file:
    file.write('some to do...')

# second way
file = open('notes.txt', 'w')
try:
    file.write('some to do 2...')
finally:
    file.close()

# other common examples are socket connections, database connections and the lock() object from threads.
from threading import Lock

lock = Lock()
with lock:  # instead of lock.acquire and lock.release
    pass


# implementing with in our classes
class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):  # what happens when enter context manager
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):  # what happens when exit context manager
        if self.file:
            self.file.close()
        print('exc:', exc_type, exc_val)
        if exc_type is not None:
            print('exception treated')
        print('exit')
        return True



with ManagedFile('notes.txt') as file:
    print('do some stuff')
    file.write('test text')
    file.somemethod()  # invalid method


print('continuing here')


# we can implement context manager as decorator for a function instead of a class
from contextlib import contextmanager
@contextmanager
def open_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()


with open_file('notes.txt') as file:
    file.write('write some more stuff...')
