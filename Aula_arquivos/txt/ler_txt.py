
matriz = []

with open("./Aula_arquivos/func1.txt", "r") as arquivos:
    for linha in arquivos:
        lista = (linha.split("\t"))
        matriz.append(lista)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{matriz [i][j]}\t\t", end = "")
    print()