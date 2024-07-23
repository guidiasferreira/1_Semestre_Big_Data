
import pickle

try:
    arq = open("./arquivos_aula/funcionario_1.bi", "rb")
    lista_funcionarios = pickle.load(arq)
    arq.close()

    for i in range(len(lista_funcionarios)):
        for j in range(len(lista_funcionarios[i])):
            print(f"{lista_funcionarios [i] [j]}\t\t", end = " ")
        print()

except IOError:
    print(f"Error! arquivo não existe")
    