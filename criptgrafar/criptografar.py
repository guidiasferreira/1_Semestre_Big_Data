
from cryptography.fernet import Fernet

chave = Fernet.generate_key()

with open("./criptgrafar/senha3.key", "wb") as arquiochave:
    arquiochave.write(chave)
