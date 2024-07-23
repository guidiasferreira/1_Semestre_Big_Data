
lista_funcionarios = []
n = int(input("Insira o número de funcionários: "))

for i in range(n):
    lista = [None] * 3
    lista[0] = input(f"Insira o nome do {i+1}\u00BA funcionário: ")
    lista[1] = float(input(f"Insira o salário do {i+1}\u00BA funcionário: "))
    lista[2] = int(input(f"Insira o número de dependentes do {i+1}\u00BA funcionário: "))
    lista_funcionarios.append(lista)


with open("./teste/func1.txt", "w+") as arquivos:
    for nome, salario, dependentes in lista_funcionarios:
        arquivos.writelines(f"{nome}\t {salario}\t {dependentes}\n")
