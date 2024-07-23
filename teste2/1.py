
lista_func = []
n = int(input("Insira a quantidade de funcionários: "))

for i in range(n):
    lista = [None] * 3
    lista[0] = input("Insira o nome: ")
    lista[1] = float(input("Insira o salário: "))
    lista[2] = int(input("Insira o número de dependentes: "))
    lista_func.append(lista)

with open("./a/1.txt", "a+") as arquivo:
    for nome, salario, dependentes in lista_func:
        arquivo.writelines(f"{nome} {salario}\t\t {dependentes}\n")