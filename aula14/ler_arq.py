
matriz = []
arquivo_lista = open("aula14/funcionarios.txt", "r")

for linha in arquivo_lista:
    lista = (linha.split("\t"))
    matriz.append(lista)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j != 0:
            matriz [i] [j] = float(matriz [i] [j])
        print("{}\t\t" .format(matriz [i] [j]), end = "  ")
    print("")

arquivo_lista.close()