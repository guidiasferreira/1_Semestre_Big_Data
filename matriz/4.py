
n = int(input("Entre com o número de linhas: "))
m = int(input("Entre com o número de colunas: "))

matriz = [[0 for l in range(m)] for c in range (n)]

for l in range(n):
    for c in range(m):
        matriz [l] [c] = int(input(f"Elemento [{l}][{c}]= "))
print(matriz)

soma = 0

for l in range(n):
    for c in range(m):
        soma = soma + matriz [l] [c]
        
media = soma / (n * m)

print(f"A soma dos elementos da matriz = {soma}")
print(f"A média dos elementos da matriz = {media}")

soma = 0

for l in range(n):
    soma = soma + sum(matriz[l])
print(soma)