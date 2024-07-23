
matriz = []

with open("./arquivos/funcionario1.txt", "r") as f:

    for linha in f:
        lista = (linha.split("\t"))
        matriz.append(lista)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):

        print(f"{matriz [i][j]}\t", end = "")
    print("")
