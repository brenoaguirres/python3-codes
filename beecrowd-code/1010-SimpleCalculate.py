product_a = input().split()
product_b = input().split()

print(f"""VALOR A PAGAR: R$ {(float(product_a[1]) * float(product_a[2])) + 
    (float(product_b[1]) * float(product_b[2])):.2f}""")

