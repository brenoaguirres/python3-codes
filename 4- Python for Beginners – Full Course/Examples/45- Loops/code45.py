# Loops
# while vs. for

condition = True
control = 0
while condition:
    print("The condition is True")
    control += 1
    if control > 10:
        condition = False

print("After the loop")


count = 0
while count < 10:
    print("Inside loop")
    count = count + 1
print("After the loop")


items = [1, 2, 3, 4]
for item in items:  # iterable
    print(item)

for item in range(15):
    print(item)

items = ["Beau", "Syd", "Quincy"]
for index, item in enumerate(items):
    print(index, item)

