
import pickle

try:
    with open("./estudos_prova/prova1.bi", "rb") as arquivos:
        lista_funcionarios = pickle.load(arquivos)

except IOError:
    lista_funcionarios = []


opcao = "S"

while opcao == "S" or opcao == "s":
    lista = [None] * 3
    lista[0] = input("Insira o nome do funcionário: ")
    lista[1] = float(input("Insira o salário do funcionário: "))
    lista[2] = int(input("Insira o número de dependentes: "))
    lista_funcionarios.append(lista)
    opcao = input("Deseja continuar? S/N: ")

with open("./estudos_prova/prova1.bi", "wb") as arquivos:
    pickle.dump(lista_funcionarios, arquivos)