
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz [l] [c] = int(input(f"Insira os elementos {[l]} {[c]}: "))

print("-=" * 30)
for linha in matriz:
    print(linha)

produto = 1

for l in range(0, 3):
    for c in range(0, 3):
        produto = produto * matriz [l] [c]

print(f"O produto dos elementos da matriz = {produto}")

for l in range(len(matriz)):
    produto = 1
    for elemento in matriz [l]:
        produto = produto * elemento
    print(f"O produto da {l+1}\u00BA linha = {produto}")