
n = int(input("Insira o número de indústrias: "))
m = int(input("Insira o número de clientes: "))

demanda = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        demanda [i][j] = float(input(f"Insira o valor das demandas {[i]} {[j]}: "))

print("-" * 30)

for linha in demanda:
    print(linha)

soma_demanda = 0
soma_demanda2 = 0
media = 0

for i in range(n):
    for j in range(m):
        if n == m:
            if i == j:
                soma_demanda += demanda [i][j]
            
            if i + j == n - 1:
                soma_demanda2 += demanda [i][j]
            media = soma_demanda2 / n

print(f"A soma das demandas = {soma_demanda}\nA média das demandas = {media}")
