
n = int(input("Entre com o número de linhas: "))
m = int(input("Entre com o número de colunas: "))

matriz = [[0 for l in range(m)] for c in range (n)]

for l in range(n):
    for c in range(m):
        matriz [l] [c] = int(input(f"Elemento [{l}][{c}]= "))
print(matriz)

soma = 0

for l in range(n):
    print(f"A soma dos elementos da {l+1}\u00BA linha = {sum(matriz[l])}")
    
for l in range(n):
    print(f"A média dos elementos da matriz = {sum(matriz[l]) / len(matriz[l])}")

for l in range(n):
    print(f"O maior dos elementos da matriz = {max(matriz[l])}")

for l in range(n):
    print(f"O menor dos elementos da matriz = {min(matriz[l])}")

for l in range(n):
    soma = 0
    for c in range(m):
        soma = soma + matriz [l] [c]
    print(f"Coluna {l+1} a soma = {soma}")