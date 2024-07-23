
n = int(input("Entre com o número de linhas: "))
m = int(input("Entre com o número de colunas: "))
auxiliar = [0] * m

matriz = [[0 for i in range(m)] for j in range (n)]
print(matriz) 
for i in range(n):
    for j in range(m):
        matriz [i][j] = int(input(f"Elemento [{i}][{j}]= "))

print(matriz)