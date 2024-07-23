
teste = []

teste.append("Gustavo")
teste.append(19)

galera = []

galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 45
galera.append(teste[:])
print(galera)