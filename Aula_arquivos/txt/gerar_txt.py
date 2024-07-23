
lista_funcionarios = []
n = int(input("Insira o número de funcionários: "))

for linha in range(n):
    lista = [None] * 3
    lista[0] = input(f"Insira o nome do {linha+1}\u00AA funcionário: ")
    lista[1] = float(input(f"Insira o salário do {linha+1}\u00AA funcionário: "))
    lista[2] = int(input(f"Insira o número de dependentes {linha+1}\u00AA funcionário: "))
    lista_funcionarios.append(lista)

with open ("./Aula_arquivos/func1.txt", "a+") as arquivos:
    for nome, salario, dependentes in lista_funcionarios:
        arquivos.writelines(f"{nome}\t {salario}\t {dependentes}\n")