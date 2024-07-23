
import pickle
from time import sleep

def menu():
    print("MENU:\n")
    print("1 - Cadastrar funcionário")
    print("2 - Consultar total salário dos funcionários")
    print("3 - Excluir Funcionário")
    print("4 - Alterar salário do funcionário")
    print("5 - Ordernar funcionários")
    print("6 - Consultar os funcionários")
    print("7 - Sair")


def cadastrar():
    try:
        with open("./funcao/funcionarios2.bi", "rb") as arquivos:
            lista_funcionarios = pickle.load(arquivos)
        
    except IOError:
        lista_funcionarios=[] 
        
    opcao = "S"
    
    while opcao == "s" or opcao == "S":
        lista = [None] * 3
        lista[0] = input(f"Entre com o nome do funcionario: ")
        lista[1] = float(input(f"Entre com o salario funcionario: "))
        lista[2] = int(input(f"Entre com número de dependentes do funcionario: "))
        lista_funcionarios.append(lista) 
        opcao = input("Quer cadastrar outro funcionario S/N: ")
        
    with open("./funcao/funcionarios2.bi", "wb") as arquivos:     
        pickle.dump(lista_funcionarios, arquivos) 

def consultar_total_dos_salarios():
    try:
        with open("./funcao/funcionarios2.bi", "rb") as arquivos:
            lista_funcionarios = pickle.load(arquivos)
        total = 0
        
        for i in range(len(lista_funcionarios)):
            total = total + lista_funcionarios [i][1]
            for j in range(len(lista_funcionarios [i])): 
                print("{}\t\t" .format(lista_funcionarios [i][j]), end = " ") 
            print("")
        print(f"O total dos salários = {total :.2f}")    
        
    except IOError:
        print("Não tem dados de funcionários cadastrados")   

def consultar_funcionarios():
    try:
        with open("./funcao/funcionarios2.bi", "rb") as arquivos:
            lista_funcionarios = pickle.load(arquivos)
        
        for i in range(len(lista_funcionarios)):
            for j in range(len(lista_funcionarios [i])): 
                print("{}\t\t" .format(lista_funcionarios [i][j]), end = " ") 
            print("")   
        
    except IOError:
        print("Não tem dados de funcionários cadastrados")   
              
                      
def excluir_funcionario():
    try:
        with open("./funcao/funcionarios2.bi", "rb") as arquivos:
            lista_funcionarios = pickle.load(arquivos)
    
        nao_encontrou = True
        nome = input("Entre com o nome do funcionario para excluir: ")
        
        for i in range(len(lista_funcionarios)):
            if nome==lista_funcionarios[i][0]:
                lista_funcionarios.pop(i)
                nao_encontrou=False
                break
            
        if nao_encontrou:
            print(f"Nao existe o funcionario {nome}")
            sleep(1)   
            
        else:
            with open("./funcao/funcionarios2.bi", "wb") as arquivos: 
                pickle.dump(lista_funcionarios, arquivos)  
                         
    except IOError:
        print("Erro no arquivo!")    
        

def alterar__salario_funcionario():
    try:
        with open("./funcao/funcionarios2.bi", "rb") as arquivos:
            lista_funcionarios = pickle.load(arquivos)
    
        nao_encontrou = True
        nome = input("Entre com o nome do funcionario para alterar: ")
        
        for i in range(len(lista_funcionarios)):
            if nome == lista_funcionarios [i][0]:
                print(f"Salário anterior = {lista_funcionarios [i][1]}")
                lista_funcionarios [i][1] = float(input("Entre com o novo salário: "))
                nao_encontrou = False
                break
            
        if nao_encontrou:
            print(f"Nao existe o funcionario {nome}")
            sleep(1)   
            
        else:
            with open("./funcao/funcionarios2.bi", "wb") as arquivos: 
                pickle.dump(lista_funcionarios, arquivos)     
                      
    except IOError:
        print("Erro no arquivo!")

def ordernar_funcionario():
    try:
        with open("./funcao/funcionarios2.bi", "rb") as arquivos:
            lista_funcionarios = pickle.load(arquivos)
            
            i = int(input("Entre com a opção 0 - pelo nome e 1 pelo salário: "))
            
            if i == 0:
                lista_funcionarios.sort(key = lambda r: r[0])
            
            elif i == 1:
                lista_funcionarios.sort(key = lambda r: r[1])
            
            else:
                print(f"Opção {i} inválida!")
            
            with open("./funcao/funcionarios2.bi", "wb") as arquivos:
                pickle.dump(lista_funcionarios, arquivos)               
                
    except IOError:
        print("Erro no arquivo!")
        
opc=True

while opc:
    menu()
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        cadastrar()  
        sleep(1)  
         
    elif escolha == "2":
        consultar_total_dos_salarios()  
        sleep(3)   
        
    elif escolha == "3":
        excluir_funcionario()  
        sleep(3)    
        
    elif escolha == "4":
        alterar__salario_funcionario()  
        sleep(3)  
    
    elif escolha == "5":
        ordernar_funcionario()  
        sleep(3)  
    
    elif escolha == "6":
        consultar_funcionarios()
        sleep(3)
        
    elif escolha == "7":
        print("Saindo...")
        sleep(1)
        opc=False
        
    else:
        print(f"Opção {escolha} inválida. Tente novamente.")
        sleep(1)