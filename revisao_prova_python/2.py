
n = int(input("Insira o número de indústrias: "))
m = int(input("Insira o número de clientes: "))

demanda = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        demanda [i][j] = float(input(f"Insira o valor em Kg do {[i]} {[j]}: "))

for linha in demanda:
    print(linha)

soma_principal = 0
soma_secundaria = 0

for i in range(n):
    for j in range(m):
        if n == m:
            if i == j:
                soma_principal += demanda [i][j]
            
            if i + j == n - 1:
                soma_secundaria += demanda [i][j]
            media = soma_secundaria / n

print(f"Soma das demandas do cliente {j} e indústria {i} = {soma_principal}\nMédia das demandas do cliente {j} e indústria {i} = {media}")