
print("AUMENTO DE SALÁRIO\n")

cargo = input("1 - Gerente\n2 - Tecnólogo\n3 - Auxiliar\n4 - Outros\n ")
salario = float(input("Digite seu salário: "))

if (cargo == "1"):
    aumento = 0.1 * salario
    cargo = "gerente"
    
elif (cargo == "2"):
    aumento = 0.2 * salario
    cargo = "tecnologo"
    
elif (cargo == "3"):
    aumento = 0.25 * salario
    cargo = "auxiliar"
    
else: 
    aumento = 0.5 * salario
    cargo = "Outros"
    
novo_salario = salario + aumento
print(f"O funcionário com o cargo de {cargo} passou a ter um salário de {novo_salario}")