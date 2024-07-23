
n = int(input("Entre com o número de funcionários: "))
i = 1
soma = 0

while i <= n:
    salario = float(input(f"Entre com o salário do {i}\u00BA funcionário: "))
    soma = soma + salario
    media = soma / n
    
    if i == 1:
        maior = salario
    
    elif maior < salario:
        maior = salario
        
        
        
    if i == 1:
        menor = salario
    
    elif menor > salario:
        menor = salario
        
    i = i + 1
    
if n!= 0:
    print(f"A soma de todos os salários = {soma :.2f}")
    print(f"A média de todos os salários = {media :.2f}")
    print(f"O maior salário = {maior :.2f}")
    print(f"O menor salário = {menor :.2f}")

else:
    print(f"Você digitou {n} para o número de funionários ")