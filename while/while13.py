
n = int(input("Entre com o número de pessoas: "))
i = 1
total = 0

 
    # ------------ TOTAL e MÉDIA------------ #

while i <= n:
    peso = float(input(f"Entre com o peso da {i}\u00BA pessoa: "))
    total = total + peso
    media = total / n


    # ------------ MAIOR------------ #
    

    if i == 1:
        maior = peso
    
    elif maior < peso:
        maior = peso
        
    # ------------ MENOR------------ #
        
              
    if i == 1:
        menor = peso
    
    elif menor > peso:
        menor = peso
        
    i = i + 1
    
if n!= 0:
    print(f"O total de pesos = {total :.2f}")
    print(f"A média de todos os pesos = {media :.2f}")
    print(f"O maior peso = {maior :.2f}")
    print(f"O menor peso = {menor :.2f}")

else:
    print(f"Você digitou {n} para o número de pessoas ")