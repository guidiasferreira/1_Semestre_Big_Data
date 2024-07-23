
matriz = []
arq_inss = open("./exe_arquivos/dadosimposto.txt", "r")

for linha in arq_inss:
    lista = (linha.split("\t"))
    matriz.append(lista)

arq_inss.close()
print(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):

        if matriz[i][j].replace(".", "", 1).isdigit() or matriz[i][j].replace(",", "", 1).isdigit():  
            matriz[i][j] = float(matriz[i][j]) 
            