
lista = []
total = 0

for i in range(0, 3):
    nome = input("Insira o nome: ")
    peso = float(input("Insira o peso: "))
    lista.append((nome, peso))

mais_pesada = lista[0]
menos_pesada = lista[0]


for pessoa in lista:
    if pessoa[1] > mais_pesada[1]:
        mais_pesada = pessoa
    if pessoa[1] < menos_pesada[1]:
        menos_pesada = pessoa

print(lista)
print(f"Total de pessoas cadastradas = {len(lista)}")
print(f"Pessoa mais pesada = {mais_pesada[1]}")
print(f"Pessoa mais leve = {menos_pesada[1]}")


