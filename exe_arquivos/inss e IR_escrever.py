
lista_imposto = []
print("Entre com os dados do INSS")

for i in range(4):
    lista = [None] * 3
    lista [0] = float(input(f"Entre com o {i+1}\u00BA valor: "))
    lista [1] = float(input(f"Entre com o {i+1}\u00BA aliquota: "))
    lista [2] = float(input(f"Entre com o {i+1}\u00BA desconto: "))
    lista_imposto.append(lista)

with open ("./exe_arquivos/dadosimposto.txt", "a+") as arq_inss:
    for valor, aliquota, desconto in lista_imposto:
        arq_inss.writelines (f"{valor}\t\t{aliquota}\t{desconto}\n")

print("Entre com os dados do IR")

lista_ir = []

for i in range(5):
    lista = [None] * 3
    lista [0] = float(input(f"Entre com o {i+1}\u00BA valor: "))
    lista [1] = float(input(f"Entre com a {i+1}\u00BA aliquota: "))
    lista [2] = float(input(f"Entre com o {i+1}\u00BA desconto: "))
    lista_ir.append(lista)

with open ("./exe_arquivos/dadosimposto.txt", "a+") as arq_inss:
    for valor, aliquota, desconto in lista_ir:
        arq_inss.writelines (f"{valor}\t\t{aliquota}\t{desconto}\n")

valor = float(input("Entre com o valor do desconto para fins de IR sobre dep: "))
with open ("./exe_arquivos/dadosimposto.txt", "a+") as arq_inss:
    arq_inss.writelines (f"{valor}\n")
