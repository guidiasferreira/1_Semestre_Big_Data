
n = int(input("Insira o número de linhas: "))
m = int(input("Insira o número de colunas: "))

matriz = [[0 for c in range(m)] for l in range(n)]

for l in range(n):
    for c in range(m):
        matriz [l][c] = int(input(f"Insira os elementos para {[l]}{[c]}: "))

print("-=" * 30)
print("MATRIZ:")

for linha in matriz:
    print(linha)

soma = 0

for l in range(n):
    for c in range(m):
        soma = soma + matriz [l][c]

for l in range(n):
    print(f"A soma da {l+1}\u00BA linha = {sum(matriz[l])}")    


for l in range(n):
    produto_par = 1
    
for elemento in matriz[l]:
    if elemento % 2 == 0:
        produto_par = produto_par * elemento
    print(f"O produto par da {l+1}\u00BA linha = {produto_par}")

for c in range(m):
    soma_coluna = 0
    for l in range(n):
        soma_coluna = soma_coluna + matriz [l][c]

    print(f"A soma da {c+1}\u00BA coluna = {soma_coluna}")

soma_principal = 0
soma_secundaria = 0

for l in range(n):
    for c in range(m):
        if n == m:
            if l == c:
                soma_principal = soma_principal + matriz [l][c]
        
            if l + c == n - 1:
                soma_secundaria = soma_secundaria + matriz [l][c]


print(f"A soma total da matriz = {soma}")
print(f"A soma da diagonal principal = {soma_principal}\nA soma da diagonal secundária = {soma_secundaria}")