
from cryptography.fernet import Fernet

with open("./Aula_arquivos/chave.key", "rb") as arquivos:
    chave = arquivos.read()

fernet = Fernet(chave)

with open("./Aula_arquivos/senhas.txt", "rb") as arquivo:
    conteudo_arquivo = arquivo.read()

criptografado = fernet.encrypt(conteudo_arquivo)

with open("./Aula_arquivos/senhas.txt", "wb") as arquivo_criptografado:
    arquivo_criptografado.write(criptografado)

