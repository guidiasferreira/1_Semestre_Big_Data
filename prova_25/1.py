
n = int(input("Insira o número de fábricas: "))
m = int(input("Insira o número de produtos: "))

estoque = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        estoque [i][j] = int(input(f"Insira o valor em toneladas {[i]} {[j]}: "))

print("-" * 30)

for linha in estoque:
    print(linha)

total_produto = 0

for i in range(n):
    for j in range(m):
        total_produto += estoque [i][j]


print(f"Total de produtos no estoque = {total_produto}")

# Calculando a quantidade média em toneladas de cada produto em todas as fábricas

for j in range(m):
    total_em_fabrica = 0
    for i in range(n):
        total_em_fabrica += estoque [i][j]

    media_produto = total_em_fabrica / n
    print(f"Quantidade média do {j+1}\u00AA produto em todas as fábricas = {media_produto}")

# Calculando a quantidade média em toneladas de cada fábrica em todos os produtos

for i in range(n):
    print(f"Quantidade média da {i+1}\u00BA fábrica em todos os produtos = {sum(estoque[i]) / m} ")
