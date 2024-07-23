
lista = []

for i in range(0, 7):
    valores = int(input("Insira os valores: "))
    lista.append(valores)

print(lista)

pares = []
impares = []

for i in lista:

    if i % 2 == 0 and i not in pares:
        pares.append(i)

    elif i % 2 == 1 and i not in impares: 
        impares.append(i)

pares.sort()
impares.sort()

print(f"Os valores pares são: {pares}")
print(f"Os valores ímpares são: {impares}")

