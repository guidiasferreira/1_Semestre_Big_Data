
n = int(input("Insira o nº  linha: "))
m = int(input("Insira o nº coluna: "))
matriz = [[0 for j in range(m)] for i in range(n)] 

for i in range(n):
    for j in range(m):
        matriz [i][j] = int(input(f"Insira os elementos da matriz {[i]} {[j]}: "))
        print(f"{matriz}", end = " ")
    print()

print("----" * 30)
print("MATRIZ: ")
for linha in matriz:
    print(linha)
