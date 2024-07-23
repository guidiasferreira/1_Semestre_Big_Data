
n = int(input("Entre com o número de pessoas: "))
i = 1
total = 0
quantidadeHomens = 0
quantidadeMulheres = 0

while i <= n:
    nome = input(f"Digite o nome da {i}\u00BA pessoa: ")
    sexo = input(f"Digite o sexo do {i}\u00BA pessoa: ")
    salario = float(input(f"Digite o salário da {i}\u00BA pessoa: "))
    
    total = total + salario
    media = total / n

    if i == 1:
        nomeFuncionarioMaior = nome
        maior = salario
    
    elif maior < salario:
        nomeFuncionarioMaior = nome
        maior = salario            
              
    if i == 1:
        nomeFuncionarioMenor = nome
        menor = salario
    
    elif menor > salario:
        nomeFuncionarioMenor = nome
        menor = salario
        
    if sexo == "M" or sexo == "F":
        quantidadeMulheres = quantidadeMulheres + 1
        
    else:
        quantidadeHomens = quantidadeHomens + 1
         
    i = i + 1
    
porcentagemM = quantidadeHomens * 100 /n
porcentagemF = quantidadeMulheres * 100 /n
    
if n!= 0:
    print(f"Nome da pessoa com maior salário = {nomeFuncionarioMaior}")
    print(f"Nome da pessoa com menor salário = {nomeFuncionarioMenor}")
    print(f"O maior salário = {maior :.2f}")
    print(f"O menor salário = {menor :.2f}")
    print(f"O total dos salários = {total :.2f}")
    print(f"A média de todos os salários = {media :.2f}")
    print(f"A porcentagem de Homens e Mulheres é: Homens {porcentagemM :.2f} e Mulheres: {porcentagemF :.2f}")
else:
    print(f"Você digitou {n} para o número de pessoas ")