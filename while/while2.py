
login = "pedro"
login_r = ""
senha = "pedro123"
senha_r = ""


while login_r != login and senha_r != senha:

    if login_r == login:
        print(f"Usuário encontrado, insira a senha")
        senha_r = input(f"Insira a senha: ")
        if senha_r == senha:
            print(f"Senha correta!")
        else:
            while senha_r != (senha):
                print(f"Senha incorreta!")
                senha_r = input(f"Insira a senha novamente: ")
    
    else:
    
        while login_r != (login):
            print(f"Login incorreto!")
            login_r = input(f"Insira o login novamente: ")
