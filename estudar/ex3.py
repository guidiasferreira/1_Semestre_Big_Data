
n = int(input("Insira o número de linhas: "))
m = int(input("Insira o número de colunas: "))

matriz = [[0 for c in range (m)] for l in range(n)]

for l in range(n):
    for c in range(m):
        matriz [l][c] = int(input(f"Insira os elementos {[l]} {[c]}: "))

print("-=" * 30)
print("MATRIZ:")

for linha in matriz:
    print(linha)

soma_diagonal = 0
soma_secundaria = 0

for l in range(n):
    for c in range(m):
        
        if n == m:
            if l == c:
                print(f"Os elementos pertencentes a diagonal principal = {matriz [l] [c]}")
                soma_diagonal = soma_diagonal + matriz [l] [c]

            if l + c == n - 1:
                print(f"Os elementos pertencentes a diagonal secundária = {matriz [l] [c]}")
                soma_secundaria = soma_secundaria + matriz [l] [c]

print(f"A soma da diagonal principal = {soma_diagonal}\nA soma da diagonal secundária = {soma_secundaria}")
