
n = int(input("Insira o número de elementos: "))
lista = []
produto = 1
soma = 0
menor = 0
soma_par = 0
soma_impar = 0
quantidade_par = 0
quantidade_impar = 0
media_impar = 0
media_par = 0
produto_somas = 0
k = 1

for i in range(n):
    elemento = int(input(f"Entre com o {i+1}\u00BA elemento da lista: "))
    lista.append(elemento)

print(lista)

for i in lista:
    produto = produto * i
    soma = soma + i
    
    if i % 2 == 1:
        
        if k == 1:
            menor = i
            k = 0
    
        elif i < menor:
            menor = i
            
    if i % 2 == 0:
        soma_par = soma_par + i
        quantidade_par = quantidade_par + 1
        media_par = soma_par / quantidade_par
        
    
    elif i % 2 == 1:
        soma_impar = soma_impar + i
        quantidade_impar = quantidade_impar + 1
        media_impar = soma_impar / quantidade_impar

produto_somas = soma_impar * soma_par

print(f"O produto dos {n} elementos = {produto}\nA soma dos {n} elementos = {soma}")
print(f"O menor número entre os ímpares = {menor}\nA soma dos pares = {soma_par}\nA soma dos ímpares = {soma_impar}")
print(f"A média dos números pares = {media_par :.2f}\nA média dos números ímpares = {media_impar :.2f}")
print(f"O produto de {soma_par} por {soma_impar} = {produto_somas}")