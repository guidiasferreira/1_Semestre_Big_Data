
lista = []

for c in range(0, 5):
    lista.append(int(input(f"Digite o número para a {c+1}\u00AA posição: ")))

    if c == 0:
        maior = lista[c]
        menor = lista[c]
    
    else:
        if lista[c] > maior:
            maior = lista[c]
        
        if lista[c] < menor:
            menor = lista[c]
    
 
print(lista)
print(f"Maior número = {maior}")
print(f"Menor número = {menor}")


for p, v in enumerate(lista):
    print(f"Na posição {p} encontrei o valor: {v}")

maior = lista[0]
menor = lista[0]

for num in lista:
    if num > maior:
        maior = num
    
    elif num < menor:
        menor = num

print(f"Maior número = {maior}")
print(f"Menor número = {menor}")