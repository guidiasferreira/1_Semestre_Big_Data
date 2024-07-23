
cargo = input("Digite seu cargo: ")
salario = float(input("Digite seu salário: "))

if cargo == ("gerente"):
    aumento = 0.1 * salario
      
elif cargo == ("tecnólogo"):
    aumento = 0.2 * salario
   
elif cargo == ("dono"):
    aumento = 0.25 * salario
    
else: 
    aumento = 0.5 * salario
    
novo_salario = salario + aumento
print(f"O funcionário com o cargo de {cargo} passou a ter um salário de {novo_salario}") 