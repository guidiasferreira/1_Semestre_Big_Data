
n = int(input("Insira o número de linhas: "))
m = int(input("Insira o número de colunas: "))

matriz_a = [[0 for c in range(m)] for l in range(n)]

for l in range(n):
    for c in range(m):
        matriz_a [l] [c] = int(input(f"Insira os elementos da matriz A {[l]} {[c]}: "))

print("-=" * 30)
print("MATRIZ A:")

for linha in matriz_a:
    print(linha)

n = int(input("Insira o número de linhas: "))
m = int(input("Insira o número de colunas: "))

matriz_b = [[0 for c in range(m)] for l in range(n)]

for l in range(n):
    for c in range(m):
        matriz_b [l] [c] = int(input(f"Insira os elementos da matriz B {[l]} {[c]}: "))
        
print("-=" * 30)
print("MATRIZ B:")

for linha in matriz_b:
    print(linha)

matriz_soma = [[0 for c in range(m)] for l in range(n)]

for l in range(n):
    for c in range(m):  
        matriz_soma[l][c] = matriz_a[l][c] + matriz_b[l][c]


print("-=" * 30)
print(f"Matriz A + Matriz B: ")
for linha in matriz_soma:
    print(linha)