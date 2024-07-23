
lista = []

quantidade = int(input("Insira a quantidade de valores: "))

for i in range(quantidade):
   elementos = int(input("Insira os valores: "))

   if elementos not in lista:
        lista.append(elementos)

lista.sort()
print(lista)