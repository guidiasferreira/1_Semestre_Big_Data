
n = int(input("Entre com o número de países: "))
i = 1
total_comercial = 0
europeu = 0
africano = 0
africano_comercial = 0

while i <= n:
    print(f"Dados do {i}\u00BA país: ")
    continente = input("Entre com o continente: ")
    balanco_comercial = float(input("Entre com o valor da balança comercial: "))
    populacao = int(input("Entre com a população: "))

    total_comercial = total_comercial + balanco_comercial
    
    if continente == "E" or continente == "e":
        europeu = europeu + 1
        
        if europeu == 1:
            maior_populacao = populacao
            
        elif populacao > maior_populacao:
            maior_populacao = populacao
            
    if continente == "F" or continente == "f":
        africano = africano + 1
        
        if balanco_comercial < 100000000:
            africano_comercial = africano_comercial + 1
    
    i = i + 1
media_comercial = total_comercial / n

if europeu > 0:
    print(f"Tem países europeus = {europeu :.2f}")
    print(f"Média comercial = {media_comercial :.2f}\nMaior população europeia = {maior_populacao}")

else:
    print(f"Não temos países europeus!")
    

if africano > 0:
   porcentagem_comercial = africano_comercial * 100 / africano
   print(f"Tem países africanos = {africano :.2f}")
   print(f"Porcentagem de países africanos com balança comercial superior a 100 milhões = {porcentagem_comercial :.2f}")

else:
    print(f"Não temos países africanos!")