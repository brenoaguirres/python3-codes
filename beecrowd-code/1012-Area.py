import math

PI = 3.14159

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

triangle_area = (a*c) / 2
circle_area = PI * math.pow(c, 2)
trapezium_area = ((a+b)*c) / 2
square_area = b*b
rectangle_area = a*b

print(f"""TRIANGULO: {triangle_area:.3f}
CIRCULO: {circle_area:.3f}
TRAPEZIO: {trapezium_area:.3f}
QUADRADO: {square_area:.3f}
RETANGULO: {rectangle_area:.3f}""")



