
n = int(input("Entre com o número de contas: "))
i = 1

while i <= n:
    print(f"Dados da {i}\u00AA conta: ")
    saldo_medio = float(input("Entre com o saldo médio: "))
    
    if saldo_medio >= 0 and saldo_medio <= 200:
        percentual = "Nenhum crédito"
        
    elif saldo_medio >= 201 and saldo_medio <= 400:
        percentual = saldo_medio * 20 / 100
        
    elif saldo_medio >= 401 and saldo_medio <= 600:
        percentual = saldo_medio * 30 / 100
        
    else:
        percentual = saldo_medio * 40 / 100

    print(f"saldo médio = {saldo_medio :.2f}\nPercentual = {percentual}")

    i = i + 1        

print("Todos dados já foram registrados!")