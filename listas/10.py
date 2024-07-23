
lista = [10, 20, 30, 40, 50]
print(lista)
print(lista.index(40))

try:
    print(lista.index(60))

except:
    print(f"O elemento 60 não está na lista")

lista.insert(2, 25)
lista.insert(5, 45)
print(lista)
lista.reverse()
print(lista)