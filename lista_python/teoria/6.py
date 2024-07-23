
galera = []
dados = []
total_maior = 0
total_menor = 0

for c in range(0, 2):
    dados.append(input("Nome: "))
    dados.append(int(input("Idade: ")))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 18:
        print(f"{p[0]} é maior de idade")
        total_maior = total_maior + 1
    else:
        print(f"{p[0]} é menor de idade")
        total_menor = total_menor + 1
print(galera)
print(f"A quantidade de pessoas maiores de idade é {total_maior}\nA quantidade de pessoas menores de idade é {total_menor}")