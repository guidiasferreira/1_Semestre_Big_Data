
with open("./aula_python/senhas2.txt", "w") as arquivos:
    senha = arquivos.writelines("1234\n1341")

with open("./aula_python/senhas2.txt", "a+") as arquivos:
    senha = arquivos.write("\nBRASIL")