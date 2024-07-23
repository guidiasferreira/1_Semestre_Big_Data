
n = int(input("Insira o número de fábricas: "))
m = int(input("Insira o número de produtos: "))

estoque = [[0 for j in range(m)]for i in range(n)]

for i in range(n):
    for j in range(m):
        estoque [i][j] = float(input(f"Insira em toneladas {[i]}{[j]}: "))

for linha in estoque:
    print(linha)

qtd_total = 0

for i in range(n):
    for j in range(m):
        qtd_total += estoque [i][j]

print(f"A quantidade total em toneladas dos produtos = {qtd_total :.2f}")

for j in range(m):
    qtd_total_prod = 0
    for i in range(n):
        qtd_total_prod += estoque [i][j]
    media = qtd_total_prod / n

    print(f"Quantidade Média em toneladas do {j+1}\u00BA Produto em todas as fábricas = {media}")
print()

for i in range(n):
    print(f"Quantidade Média em toneladas da {i+1}\u00AA Fábrica em todos os produtos = {sum(estoque[i]) / m}")
    