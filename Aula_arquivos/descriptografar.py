from cryptography.fernet import Fernet

with open("./Aula_arquivos/chave.key", "rb") as arquivos:
    chave = arquivos.read()

fernet = Fernet(chave)

with open("./Aula_arquivos/senhas.txt", "rb") as arquivo_criptografado:
    criptografado = arquivo_criptografado.read()

descriptografado = fernet.decrypt(criptografado)  

with open("./Aula_arquivos/senhas.txt", "wb") as arquivo_descriptografado:
    arquivo_descriptografado.write(descriptografado)
