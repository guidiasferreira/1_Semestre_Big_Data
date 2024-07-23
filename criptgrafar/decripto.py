
from cryptography.fernet import Fernet

with open("./criptgrafar/senha1.key", "rb") as arquiochave:
    chave = arquiochave.read()

fernet = Fernet(chave)

with open("./criptgrafar/senha1.txt", "rb") as arquivo_critografado:
    criptografado = arquivo_critografado.read()

descriptografado = fernet.decrypt(criptografado)

with open("./criptgrafar/senha1.txt", "wb") as arquio_descriptografado:
    arquio_descriptografado.write(descriptografado)