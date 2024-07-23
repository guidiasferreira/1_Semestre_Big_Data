
import pickle

try:
    with open("./arquivos/funcionario2.bi", "rb") as f:
        lista_funcionario = pickle.load(f)

    for i in range(len(lista_funcionario)):
        for j in range(len(lista_funcionario[i])):
            print(f"{lista_funcionario [i][j]}\t\t", end = " ")
        print()

except IOError:
    print(f"Erro no arquivo!")