
n = int(input("Insira o número de candidatos: "))
notas = [None] * n

for i in range(n):
    notas[i] = int(input(f"Insira a nota do {i+1}\u00BA candidato: "))

for i in range(11):
    quantidade = notas.count(i)

    if quantidade > 1:
        print(f"{quantidade} candidatos obtiveram a nota {i}")

    elif quantidade == 1:
        print(f"{quantidade} candidatos obteve a nota {i}")
    
    else:
        print(f"Nenhum candidato obteve a nota {i}")