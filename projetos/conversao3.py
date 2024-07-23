
conversao = float(input("Digite 1 para converter real para dólar" "\n" "Digite 2 para converter dólar para real" "\n" "Digite 3 para converter dólar para iene" "\n" "Digite 4 para converter iene para real "))

if conversao == 1:
    valorReal = float(input("Qual o valor em real: "))
    dolar = (valorReal / 4.95)
    print(f"Valor em dólar = {dolar :.2f}")

elif conversao == 2:    
    valorDolar = float(input("Qual o valor em dólar: "))
    real = (valorDolar * 4.95)
    print(f"Valor em real = {real :.2f}")
    
elif conversao == 3:
    valorDolar= float(input("Digite o valor em dólar: "))
    iene = (valorDolar * 150.43)
    print(f"Valor em iene = {iene :.2f}")

elif conversao == 4:
    valorIene = float(input("Digite o valor em iene"))
    real = (valorIene / 30.49)
    print(f"Valor em real = {real :.2f}")
    
else:
    print("ERRO!")
