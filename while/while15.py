
n = int(input("Entre com o número de funcionários: "))
i = 1

while i <= n:
    cargo = input("Entre com o cargo do funcionário: ")
    salario = float(input("Entre com o salário do funcionário: "))
    
    if cargo == "gerente":
        aumento = salario * 0.1
    
    elif cargo == "tecnologo":
        aumento = salario * 0.2
        
    else:
        aumento = salario * 0.25
    
    novo_salario = salario + aumento     
    
    print(f"O {i}\u00BA funcionário possui o cargo de {cargo}, ele recebia um salário de {salario :.2f}, e depois do aumento de {aumento :.2f}, ele passou a receber um salário de {novo_salario :.2f}") 
    
    i = i + 1  