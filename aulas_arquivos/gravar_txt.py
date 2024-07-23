
lista_funcionarios = []
n = int(input("Entre com a quantidade de funcionários: "))

for i in range(n):
    lista = [None] * 3
    lista [0] = input(f"Entre com o nome do {i+1}\u00BA funcionário: ")
    lista [1] = float(input(f"Entre com o salário do {i+1}\u00BA funcionário: "))
    lista [2] = int(input(f"Entre com o número de dependentes do {i+1}\u00BA funcionário: "))
    lista_funcionarios.append(lista)

with open ("./aulas_arquivos/dados_funcionarios.txt", "a+") as arqlista:
    for nome, salario, dependentes in lista_funcionarios:
        arqlista.writelines (f"{nome}\t{salario}\t{dependentes}\n")   
        