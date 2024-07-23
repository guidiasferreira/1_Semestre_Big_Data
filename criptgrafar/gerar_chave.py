
from cryptography.fernet import Fernet

chave = Fernet.generate_key()

with open("./criptgrafar/senha1.key", "wb") as arquiochave:
    arquiochave.write(chave)
