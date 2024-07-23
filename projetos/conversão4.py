
conversao = float(input("Digite 1 para converter euro pra real" "\n" "Digite 2 para converter euro pra dólar" "\n" "Digite 3 para converter euro pra pesos" "\n" "Digite 4 para converter euro pra iene"))

if conversao == 1:
    valorEuro = float(input("Digite o valor em euro: "))
    real = (valorEuro * 5.38)
    print(f"O valor em real é de {real :.2f}")

elif conversao == 2:
    valorEuro = float(input("Digite o valor em euro: "))
    dolar = (valorEuro * 1.09)
    print(f"O valor em dólar é de {dolar :.2f}")

elif conversao == 3:
    valorEuro = float(input("Digite o valor em euro: "))
    pesos = (valorEuro * 18.39)
    print(f"O valor em pesos é de {pesos :.2f}")

elif conversao == 4:
    valorEuro = float(input("Digite o valor em euro: "))
    iene = (valorEuro * 162.99)
    print(f"O valor em iene é de {iene :.2f}")

else:
    print("ERROR!")