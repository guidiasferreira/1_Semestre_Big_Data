
n = int(input("Insira o número de linhas: "))
m = int(input("Insira o número de colunas: "))

matriz_a = [[0 for c in range(m)] for l in range(n)]

for l in range(n):
    for c in range(m):
        matriz_a [l] [c] = int(input(f"Insira os elementos {[l]} {[c]}: "))

n = int(input("Insira o número de linhas: "))
m = int(input("Insira o número de colunas: "))

matriz_b = [[0 for c in range(m)] for l in range(n)]

for l in range(n):
    for c in range(m):
        matriz_b [l] [c] = int(input(f"Insira os elementos {[l]} {[c]}: "))


print("-=" * 30)
print("MATRIZ A:")
for linha in matriz_a:
    print(linha)


print("-=" * 30)
print("MATRIZ B:")
for linha in matriz_b:
    print(linha)


matriz_c = [[0 for c in range(m)] for l in range(n)]

for l in range(n):
    for c in range(m):
        matriz_c [l] [c] = matriz_a [l] [c] * matriz_b [l] [c]

print("-=" * 30)
print("MATRIZ C:")
for linha in matriz_c:
    print(linha)