
matriz = []

with open("./teste/1_txt.txt", "r+") as arquivo:

    for linha in arquivo:
        lista = (linha.split("\t"))
        matriz.append(lista)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{matriz [i][j]}\t", end = "")
    print()