
lista = []

for i in range(100):
    valores = input("Digite os valores ou 'pare' para parar: ")

    if valores == 'pare':
        break
    
    lista.append (int(valores))


print(f"Tamanho da lista = {len(lista)}")

lista.sort(reverse = True)
print(f"Lista em ordem decrescente = {lista}")

if 5 in lista:
    print(f"O valor 5 está na lista")

else:
    print(f"O valor 5 não está na lista")