
lista = [10, 20, 30, 40, 50, "A", "G"] 
print(lista)
print(lista.pop(2))
print(lista)
lista.remove(20)
print(lista)

try:
    lista.remove(30)
    
except:
    print(f"O elemento 30 não está na lista")