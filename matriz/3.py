
n = int(input("Entre com o número de linhas: "))
m = int(input("Entre com o número de colunas: "))

matriz = [[0 for l in range(m)] for c in range (n)]
print(matriz) 

#Leitura da matriz

for l in range(n):
    for c in range(m):
        matriz [l][c] = int(input(f"Elemento [{l}][{c}]= "))

#Impressão da matriz

for l in range(n):
    for c in range(m):
        print(matriz[l][c], sep = "", end = "   ")
    print("")