# global function - can be accessed anywhere
age = 8


def test():
    age2 = 10  # local function - can be accessed only inside the scope of this function
    print(age)


print(age)
test()



