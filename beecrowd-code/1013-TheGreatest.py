a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
maiorAB = (a + b + abs(a - b)) / 2
maiorAB = (maiorAB + c + abs(maiorAB - c)) / 2
maiorAB = int(maiorAB)

print(f"{maiorAB} eh o maior")

