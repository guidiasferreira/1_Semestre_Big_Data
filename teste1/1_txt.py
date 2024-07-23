
lista_funcionario = []
n = int(input("Insira a quantidade de funcionários: "))

for i in range(n):
    lista = [None] * 3
    lista[0] = input(f"Insira o nome do {i+1}\u00AA funcionário: ")
    lista[1] = float(input(f"Insira o salário do {i+1}\u00AA funcionário: "))
    lista[2] = int(input(f"Insira o número de dependentes do {i+1}\u00AA funcionário: "))
    lista_funcionario.append(lista)


with open("./teste/1_txt.txt", "a+") as arquivo:
    for nome, salario, dependentes in lista_funcionario:
        arquivo.writelines(f"{nome}\t {salario}\t {dependentes}\n")