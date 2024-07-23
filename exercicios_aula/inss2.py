
salario = float(input("Entre com o salário bruto: "))
numero_dep = int(input("Entre com o número de dependentes: "))
pensao = float(input("Entre com o valor da pensão: "))

if salario >= 0.00 and salario <= 1412.00:
    desconto_inss = (salario * 0.75)  
    inss = salario - desconto_inss
   
elif salario >= 1412.01 and salario <= 2666.68:
    desconto_inss = (salario * 0.9) - 21.18
    inss = salario - desconto_inss 
    
elif salario >= 2666.69 and salario <= 4000.03:
    desconto_inss = (salario * 0.12) - 101.18
    inss = salario - desconto_inss 
  
elif salario >= 4000.4 and salario <= 7786.02:
    desconto_inss = (salario * 0.14) - 181.18
    inss = salario - desconto_inss 
    
else:
    desconto_inss = 7786.02 * 0.14 - 181.18
    inss = salario - desconto_inss

salario_base = salario - pensao - desconto_inss - numero_dep * 189.59 

if salario_base <= 2259.20:
    imposto_renda = 0
    
elif salario_base >= 2259.21 and salario_base <= 2828.65:
    imposto_renda = salario_base * 0.075 - 169.44
    
elif salario_base >= 2828.66 and salario_base <= 3751.05:
    imposto_renda = salario_base * 0.15 - 381.44
    
elif salario_base >= 3751.06 and salario_base <= 4664.68: 
    imposto_renda = salario_base * 0.225 - 662.77
    
else:
    imposto_renda = salario_base * 0.275 - 896.00
    
salario_liquido = salario - desconto_inss - imposto_renda - pensao 

print(f"Seu salário de {salario :.2f} reais")
print(f"Com {numero_dep} dependentes")
print(f"Com {pensao} reais de pensão alimentícia")
print(f"Vai pagar de INSS {inss :.2f} reais")
print(f"Vai pagar de Imposto de renda {imposto_renda :.2f} reais")
print(f"Vai receber {salario_liquido :.2f} reais de salário liquido")