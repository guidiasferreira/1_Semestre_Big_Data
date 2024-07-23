
lista = [10, 20, 30, 40, 50]
print(lista)

try:
    print(lista.pop(1))

except:
    print(f"indice out of range")
print(lista)

try:
    lista.remove(40)
    
except:
    print(f"O elemento 60 não está na lista")
print(lista)