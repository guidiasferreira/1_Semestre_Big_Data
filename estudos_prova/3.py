
import pickle

try:
    with open("./estudos_prova/prova1.bi", "rb") as arquivos:
        lista_funcionarios = pickle.load(arquivos)

        for i in range(len(lista_funcionarios)):
            for j in range(len(lista_funcionarios[i])):
                print(f"{lista_funcionarios [i][j]}\t", end = "")
            print()

except IOError:
    print(f"ERROR!")