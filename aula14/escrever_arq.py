
lista_funcionarios = []

n = int(input("Entre com a quantidade de funcionários: "))

for i in range(n):
    lista = [None] * 3
    lista[0] = input(f"Insira o nome do {i+1}\u00BA funcionário: ")
    lista[1] = float(input(f"Insira o salário do {i+1}\u00BA funcionário: "))
    lista[2] = int(input(f"Insira o número de dependentes do {i+1}\u00BA funcionário: "))
    lista_funcionarios.append(lista)

with open("aula14/funcionarios.txt", "a+") as arquivo_lista:
    for nome, salario, dependentes in lista_funcionarios:
        arquivo_lista.writelines (f"{nome}\t {salario}\t {dependentes}\n")