
lista_func = []
n = int(input("Insira a quantidade de funcionários: "))

for i in range(n):
    lista = [None] * 3
    lista[0] = input(f"Insira o nome do {i+1}\u00BA funcionário: ")
    lista[1] = float(input(f"Insira o salário do {i+1}\u00BA funcionário: "))
    lista[2] = int(input(f"Insira o número de dependentes do {i+1}\u00BA funcionário: "))
    lista_func.append(lista)

with open("./arquivos2/lista1", "a+") as arquivos:
    for nome, salario, filhos in lista_func:
        arquivos.writelines(f"{nome}\t {salario}\t {filhos}\n")
