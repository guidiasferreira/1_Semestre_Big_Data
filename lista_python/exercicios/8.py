
n = int(input("Insira o número de elementos: "))
lista = []
produto = 1

for i in range(n):
    elementos = int(input(f"Insira o {i+1}\u00BA elemento da lista: "))
    lista.append(elementos)

k = 1
menor = 0
qtd_maior = 0
qtd_igual = 0
qtd_menor = 0
soma_par = 0
qtd_par = 0

for i in lista:
    produto = produto * i

    if i % 2 == 1:
        if k == 1:
            menor = i
            k = 2
        elif i < menor:
            menor = i

    if i % 2 == 0:
        qtd_par = qtd_par + 1
        soma_par = soma_par + i

    if i > 0:
        qtd_maior = qtd_maior + 1
    
    elif i == 0:
        qtd_igual = qtd_igual + 1
    
    else:
        qtd_menor = qtd_menor + 1

porcentagem_maior = qtd_maior * 100 / n
porcentagem_igual = qtd_igual * 100 / n
porcentagem_menor = qtd_menor * 100 / n
media = soma_par / qtd_par

print(f"O produto dos elementos são {produto}\nO menor elemento ímpar é {menor}")
print(f"Porcentagem de elementos maiores que 0 = {porcentagem_maior :.2f}\nPorcentagem de elementos igual a 0 = {porcentagem_igual :.2f}")
print(f"Porcentagem de elementos menores que 0 = {porcentagem_menor :.2f}\nMédia aritmética dos elementos pares = {media}")