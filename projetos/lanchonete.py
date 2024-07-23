
print("Lanchonete")
print("1 - Hamburguer\n2 - Xburguer\n3 - Xsalada\n4 - Xbacon\n5 - Xtudo")

codigo_lanche = int(input("Qual o código do lanche: "))
quantidade = int(input("Qual a quantidade: "))

if (codigo_lanche == 1):
    valor = 10
    preco = valor * quantidade
    nome_lanche = "Hamburguer"
    
elif (codigo_lanche == 2):
    valor = 15
    preco = valor * quantidade
    nome_lanche = "X-burguer"

elif (codigo_lanche == 3):
    valor = 18
    preco = valor * quantidade
    nome_lanche = "X-salada"

elif (codigo_lanche == 4):
    valor = 20
    preco = valor * quantidade
    nome_lanche = "X-bacon"
   
elif (codigo_lanche == 5):
    valor = 35
    preco = valor * quantidade
    nome_lanche = "X-tudo"

else: 
    print("Código inexistente")
    
if (codigo_lanche >= 1 and codigo_lanche <= 5):
    print(f"O valor a ser pago pelos {quantidade} lanches de {nome_lanche} = {preco} reais")
    