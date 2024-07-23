
matriz = []

with open("./revisao_prova_python/funcionario1.txt", "r+") as arquivo:
    for linha in arquivo:
        lista = (linha.split("\t"))
        matriz.append(lista)
    
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{matriz [i][j]}\t", end = " ")
    print()