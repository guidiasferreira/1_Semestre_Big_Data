
n = int(input("Insira o número de clientes: "))
gastos = [0] * n
print(gastos)

for i in range(n):
    print(i)
    gastos[i] = float(input("Insira o valor dos gastos: "))
    print(gastos)

gastos.sort()
print(gastos)

gastos.sort(reverse = True)
print(gastos)


