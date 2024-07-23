
n = int(input("Entre com o número de pessoas: "))
i = 1
totalVendas = 0

while i <= n:
    tipoLanche = input("Qual o lanche desejado: ")
    quantidade = int(input("Entre com a quantidade de lanches: "))
    
    if tipoLanche == "hamburguer":
        valor = 15
        total = valor * quantidade
        
    elif tipoLanche == "x-burguer":
        valor = 20
        total = valor * quantidade
      
    elif tipoLanche == "hot_dog":
        valor = 10
        total = valor * quantidade
     
    else:
        valor = 30
        total = valor * quantidade
        

    totalVendas = totalVendas + total
    mediaVendas = totalVendas / n
           
    print(f"A {i}\u00AA pessoa comprou {quantidade} {tipoLanche} de {valor :.2f} reais, e vai pagar um total de = {total :.2f} reais\n")
    
    i = i + 1
    
print(f"\nTotal de vendas = {totalVendas :.2f} reais")
print(f"Média de vendas = {mediaVendas :.2f} reais")