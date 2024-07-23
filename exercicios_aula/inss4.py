
produto = input("Entre com o nome do produto: ")
valor_venda = float(input("Entre com o valor de vendas: "))
quantidade = int (input("Entre com a quantidade: "))

total = valor_venda * quantidade

if valor_venda <= 10000:
    comissao = total * 0.10
    
elif valor_venda <= 30000:
    comissao = total * 0.09 + 200
    
elif valor_venda <= 50000:
    comissao = total * 0.07 + 1000
    
else:
    comissao = total * 0.05 + 2500
print(f"Produto escolhido foi {produto}, valor de venda total foi de {valor_venda :.2f}, e a comissão adquirida foi de {comissao :.2f}")
    