
lista1 = []
lista1.append(60)
lista1.append(90)
print(lista1)

lista2 = [5, 5, 4]
lista1.extend(lista2)
print(lista1)

cl = lista1.count(5)
print(f"A quantidade de elementos 5 na lista = {cl}")