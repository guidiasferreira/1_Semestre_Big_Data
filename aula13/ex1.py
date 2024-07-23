
n = int(input("Insira o número de linhas: "))
m = int(input("Insira o número de colunas: "))

matriz = [[0 for c in range(m)] for l in range(n)]

for l in range(n):
    for c in range(m):
        matriz [l] [c] = int(input(f"Insira os elementos {[l]} {[c]}: "))

print("-=" * 30)
print("MATRIZ:")

for linha in matriz:
    print(linha)

soma = 0
produto_impar = 1
soma_diagonal = 0
soma_secundaria = 0

for l in range(n):
    for c in range(m):
        soma = soma + matriz [l] [c]

        if matriz [l] [c] % 2 == 1:
            produto_impar = produto_impar * matriz [l] [c]
        
        if n == m:
            if l == c:
                soma_diagonal = soma_diagonal + matriz [l] [c]
        
            if l + c == n - 1:
                soma_secundaria = soma_secundaria + matriz [l] [c] 

media = soma_diagonal / n

for c in range(m):
    soma_coluna = 0
    for l in range(n):
        soma_coluna = soma_coluna + matriz [l] [c]

    print(f"A soma da {c+1}\u00BA coluna = {soma_coluna}")

print(f"A soma dos elementos da matriz = {soma}\nO produto dos elementos ímpares = {produto_impar} ")
print(f"Média aritmética da diagonal principal = {media}\nA Soma dos elementos da diagonal secundária = {soma_secundaria}")
