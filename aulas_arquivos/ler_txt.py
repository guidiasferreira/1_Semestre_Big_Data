
matriz = []
arqlista = open("./aulas_arquivos/dados_funcionarios.txt", "r")

for linha in arqlista:
    lista = (linha.split("\t"))
    matriz.append(lista)

arqlista.close()

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j == 1:
            matriz [i] [j] = float(matriz [i] [j])
        
        elif j == 2:
            matriz [i] [j] = int(matriz [i] [j])
        print(f"{matriz [i] [j]}\t" , end = " ")
    print()
    