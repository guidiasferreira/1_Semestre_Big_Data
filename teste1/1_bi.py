
import pickle

try:
    with open("./teste/1_bi", "rb") as arquivo:
        lista_funcionario = pickle.load(arquivo)

except IOError:
    lista_funcionario = []


opcao = "S"

while opcao == "S" or opcao == "s":
    lista = [None] * 3
    lista[0] = input("Insira o nome: ")
    lista[1] = float(input("Insira o salário: ")) 
    lista[2] = int(input("Insira o número de dependentes: "))
    lista_funcionario.append(lista)
    opcao = input("Deseja continuar? S/N: ")
with open("./teste/1_bi", "wb") as arquivo:
    pickle.dump(lista_funcionario, arquivo)
