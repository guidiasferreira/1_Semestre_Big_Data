
n = int(input("Insira o número de produtos: "))
m = int(input("Insira o número de armazéns: "))

armazenamento = [[0 for c in range(m)] for l in range(n)]

total_armazenado = 0

for l in range(n):
    for c in range(m):
        armazenamento [l] [c] = int(input(f"Insira os elementos {[l]} {[c]}: "))
        total_armazenado = total_armazenado + armazenamento [l] [c]

print("-=" * 30)
print("ARMAZÉM:")

for linha in armazenamento:
    print(linha)

media = total_armazenado / (n * m)


for l in range(n):
    print(f"Total em toneladas do {l+1}\u00AA armazém = {sum(armazenamento[l])}")

for c in range(m):
    total_produto = 0
    for l in range(n):
        total_produto = total_produto + armazenamento [l] [c]

    print(f"Total em toneldas do {c+1}\u00AA produto = {total_produto}")

print(f"Total armazenado em todos os armazéns = {total_armazenado}\nMédia dos produtos em toneladas = {media}")