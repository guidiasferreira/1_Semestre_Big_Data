
n = int(input("Insira o número de funcionários: "))
lista_funcionarios = []

for i in range(n):
    lista = [None] * 3
    lista[0] = input(f"Insira o nome do {i+1}\u00BA funcionário: ")
    lista[1] = float(input(f"Insira o salário do {i+1}\u00BA funcionário: "))
    lista[2] = int(input(f"Insira o número de dependentes do {i+1}\u00BA funcionário: "))
    lista_funcionarios.append(lista)

with open("./revisao_prova_python/funcionario1.txt", "a+") as arquivo:
    for nome, salario, dependentes in lista_funcionarios:
        arquivo.writelines(f"{nome}\t {salario}\t {dependentes}\n")