from cryptography.fernet import Fernet

# Carrega a chave de criptografia
with open("./criptgrafar/senha1.key", "rb") as arquivo_chave:
    chave = arquivo_chave.read()

# Cria uma instância do objeto Fernet com a chave carregada
fernet = Fernet(chave)

# Abre o arquivo criptografado
with open("./criptgrafar/senha1.txt", "rb") as arquivo_criptografado:
    texto_criptografado = arquivo_criptografado.read()

# Tenta descriptografar os dados
try:
    texto_descriptografado = fernet.decrypt(texto_criptografado)
except Exception as e:
    print("Erro durante a descriptografia:", e)
else:
    # Escreve os dados descriptografados em um novo arquivo
    with open("./criptgrafar/senha1_descriptografado.txt", "wb") as arquivo_descriptografado:
        arquivo_descriptografado.write(texto_descriptografado)
