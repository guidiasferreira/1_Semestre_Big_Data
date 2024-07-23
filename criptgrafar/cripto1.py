
from cryptography.fernet import Fernet

with open("./criptgrafar/senha1.key", "rb") as arquiochave:
    chave = arquiochave.read()

fer = Fernet(chave)

with open("./criptgrafar/senha1.txt", "rb") as arquiochave:
    dados_arquivo = arquiochave.read()

criptografado = fer.encrypt(dados_arquivo)

with open("./criptgrafar/senha1.txt", "wb") as arquivo_criptografado:
    arquivo_criptografado.write(criptografado)