
n = int(input("Insira a quantidade de produtos: "))
m = int(input("Insira a quantidade de armazéns: "))

matriz = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
      matriz [i] [j] = int(input(f"Peso do produto = [{i}] [{j}] = ")) 
      
print(matriz)

toneladas = 0

for i in range(n):
    toneladas = toneladas + sum(matriz[i])
    
print(f"O total armazenado em toneladas é {toneladas}")  
print(f"A média em toneladas dos produtos = {toneladas / (n * m) :.2f}")
print(f"Armazém {i+1} o total = {sum(matriz[i])}")


for j in range(m):
    toneladas = 0
    for i in range(n):
        toneladas = toneladas + matriz [i] [j]
    print(f"Soma de cada produto = {toneladas}")