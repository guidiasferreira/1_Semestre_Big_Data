
a = float (input("Entre com o primeiro número: "))
b = float (input("Entre com o segundo número: "))
c = float (input("Entre com o terceiro número: "))

if (a > b):
    if (a > c):
        print(f"Maior = {a}")
    else:
        print(f"Maior = {c}")
        
else:
    if (b > c):
        print(f"Maior = {b}")
    else:
        print(f"\nMaior = {c}")
        print("FIM")