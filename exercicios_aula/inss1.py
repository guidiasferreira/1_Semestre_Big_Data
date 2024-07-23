
salario_bruto = float(input("Entre com o salário bruto: "))

if salario_bruto >= 0.00 and salario_bruto <= 1412.00:
    desconto_inss = (salario_bruto * 0.75)  
    inss = salario_bruto - desconto_inss
   
elif salario_bruto >= 1412.01 and salario_bruto <= 2666.68:
    desconto_inss = (salario_bruto * 0.9) - 21.18
    inss = salario_bruto - desconto_inss 
    
elif salario_bruto >= 2666.69 and salario_bruto <= 4000.03:
    desconto_inss = (salario_bruto * 0.12) - 101.18
    inss = salario_bruto - desconto_inss 
  
elif salario_bruto >= 4000.4 and salario_bruto <= 7786.02:
    desconto_inss = (salario_bruto * 0.14) - 181.18
    inss = salario_bruto - desconto_inss 
    
else:
    desconto_inss = (7786.02 * 0.14) - 181.18
print(f"O salário de {salario_bruto :.2f} reais deve pagar {desconto_inss :.2f} reais de {inss} ")
