
import pickle

try:
    with open("./teste/1_bi", "rb") as arquivo:
        lista_funcionario = pickle.load(arquivo)

    for i in range(len(lista_funcionario)):
        for j in range(len(lista_funcionario[i])):
            print(f"{lista_funcionario [i][j]}\t\t", end = " ")
        print()

except IOError:
    print(f"ERRO!")