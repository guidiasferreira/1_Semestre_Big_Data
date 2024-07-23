
n = int(input("Insira o número de clientes: "))
gastos = [None] * n

for i in range(n):
    gastos[i] = float(input("Insira o valor dos gatos: "))

gastos.sort()
print(f"Gastos em ordem crescente = {gastos :.2f}")

gastos.sort(reverse = True)
print(f"Gastos em ordem decrescente = {gastos :.2f}")

