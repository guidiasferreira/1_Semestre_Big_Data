
valores = []

for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for p, v in enumerate(valores):
    print(f"Na posição {p} encontrei o valor {v}")
print("Chguei ao fim!")