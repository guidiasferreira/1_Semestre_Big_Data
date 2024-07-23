
import pickle

try:
    with open("./arquivos/funcionario2.bi", "rb") as f:
        lista_funcionario = pickle.load(f)

except IOError:
    lista_funcionario = []

opcao = "S"

while opcao == "S" or opcao == "s":
    lista = [None] * 3
    lista[0] = input(f"Insira o nome do funcionário: ")
    lista[1] = float(input(f"Insira o salário do funcionário: "))
    lista[2] = int(input(f"Insira o número de dependentes: "))
    lista_funcionario.append(lista)
    opcao = input(f"Deseja continuar? S/N: ")

with open("./arquivos/funcionario2.bi", "wb") as f:
    pickle.dump(lista_funcionario, f)