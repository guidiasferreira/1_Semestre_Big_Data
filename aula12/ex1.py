
n = int(input("Insira o número de linhas: "))
m = int(input("Insira o número de colunas: "))

matriz = [[0 for c in range(m)] for l in range(n)]

soma = 0

for l in range(n):
    for c in range(m):
        matriz [l] [c] = int(input(f"Insira os elementos [{l}] [{c}]: "))
        soma = soma + matriz [l] [c]

print("-=" * 30)
for linha in matriz:
    print(linha)

media = soma / (n * m)


for l in range(n):
    print(f"A soma da {l+1}\u00BA linha = {sum(matriz[l])}")


for c in range(m):
    soma_coluna = 0
    for l in range(n):
        soma_coluna = soma_coluna + matriz [l] [c]
    print(f"A soma da {c+1}\u00BA coluna = {soma_coluna}")

print(f"A soma de todos os elementos da matriz = {soma}\nMédia da matriz = {media}")