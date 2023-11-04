items = ["Roger", "Syd", "Quincy", "bob"]
items[1:1] = ["Benjamin", "Frank"]

itemscopy = items[:]  # copy list

items.sort(key=str.lower)  # cannot sort between different dtypes; sorts uppercase first, lowercase last
# key=str.lower allows to bypass this difference of upper and lower upon sorting


print(items)
print(itemscopy)

print(sorted(itemscopy, key=str.lower))  # will not modify the original list
print(itemscopy)



