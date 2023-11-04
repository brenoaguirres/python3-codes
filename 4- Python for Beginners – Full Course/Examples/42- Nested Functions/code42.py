# Nested functions
# -- only visible inside the function
# -- used to create utilities just for this function
# -- useful for closures


def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split()
    for word in words:
        say(word)


talk('I am going to buy the milk')


# accessing local variables inside inner function scope with non-local keyword


def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()


count()



