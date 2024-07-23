
lista_funcionario = []
n = int(input("Insira a quantidade de funcionários: "))

for i in range(n):
    lista = [None] * 3
    lista[0] = input(f"Entre com o nome do {i+1}\u00AA funcionário: ")
    lista[1] = float(input(f"Entre com o salário do {i+1}\u00AA funcionário: "))
    lista[2] = int(input(f"Entre com o número de dependentes do {i+1}\u00AA funcionário: "))
    lista_funcionario.append(lista)

with open("./arquivos/funcionario1.txt", "a+") as arqlista:
    for nome, salario, dependentes in lista_funcionario:
        arqlista.writelines(f"{nome}\t {salario}\t {dependentes}\n")

