
lista = []

for i in range(0, 5):
    valores = int(input("Insira os valores: "))
    lista.append(valores)
    lista.sort()
print(f"Os valores digitados são = {lista}")