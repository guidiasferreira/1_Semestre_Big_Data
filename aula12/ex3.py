
n = int (input("Insira o número de linhas: "))
m = int(input("Insira o número de colunas: "))

matriz = [[0 for c in range(m)] for l in range(n)]

for l in range(n):
    for c in range(m):
        matriz [l] [c] = int(input(f"Insira os elementos {[l]} {[c]}: "))

print("-=" * 30)
print("Matriz:")

for linha in matriz:
    print(linha)

soma_principal = 0
soma_secundaria = 0

for l in range(n):
    for c in range(m):
        
        if n == m:
            if l == c:
                soma_principal = soma_principal + matriz [l] [c]
        
            if l + c == n - 1:
                soma_secundaria = soma_secundaria + matriz [l] [c]


print(f"A soma da diagonal principal é {soma_principal}\nA soma da diagonal secundária é {soma_secundaria}")
  