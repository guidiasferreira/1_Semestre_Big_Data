from cryptography.fernet import Fernet

chave = Fernet.generate_key()

with open("./Aula_arquivos/chave.key", "wb") as arquivos:
    arquivos.write(chave)