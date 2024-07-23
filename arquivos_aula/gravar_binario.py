
import pickle

try:
    arq = open ("./arquivos_aula/funcionario_1.bi", "rb")
    lista_funcionario = pickle.load(arq)
    arq.close()    

except IOError:
    lista_funcionario = []

opcao = "S"

while opcao == "S" or opcao == "s":
    lista = [None] * 3
    lista [0] = input(f"Entre com o nome do funcionário: ")
    lista [1] = float(input(f"Entre com o salário do funcionário: "))
    lista [2] = int(input(f"Entre com o número de dependentes: "))
    lista_funcionario.append(lista)
    opcao = input("Deseja cadastrar um novo funcionário? S/N: ")

with open("./arquivos_aula/funcionario_1.bi", "wb") as arq:
    pickle.dump(lista_funcionario, arq)
    