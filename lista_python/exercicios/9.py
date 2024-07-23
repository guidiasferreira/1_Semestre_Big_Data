
lista = []

for i in range(0, 5):
    nota = float(input(f"Insira a nota do {i+1}\u00AA candidato: "))
    lista.append(nota)
print(lista)

qtd1 = 0
qtd2 = 0
qtd3 = 0
qtd4 = 0
qtd5 = 0
qtd6 = 0
qtd7 = 0
qtd8 = 0
qtd9 = 0
qtd10 = 0

for nota in lista:

    if nota == 1:
        qtd1 = qtd1 + 1
    
    elif nota == 2:
        qtd2 = qtd2 + 1
    
    elif nota == 3:
        qtd3 = qtd3 + 1
    
    elif nota == 4:
        qtd4 = qtd4 + 1
    
    elif nota == 5:
        qtd5 = qtd5 + 1
    
    elif nota == 6:
        qtd6 = qtd6 + 1
    
    elif nota == 7:
        qtd7 = qtd7 + 1
    
    elif nota == 8:
        qtd8 = qtd8 + 1
    
    elif nota == 9:
        qtd9 = qtd9 + 1
    
    elif nota == 10:
        qtd10 = qtd10 + 1
    
    
print("Quantidade de candidatos por nota:")
print(f"Nota 1: {qtd1} candidato(s)")
print(f"Nota 2: {qtd2} candidato(s)")
print(f"Nota 3: {qtd3} candidato(s)")
print(f"Nota 4: {qtd4} candidato(s)")
print(f"Nota 5: {qtd5} candidato(s)")
print(f"Nota 6: {qtd6} candidato(s)")
print(f"Nota 7: {qtd7} candidato(s)")
print(f"Nota 8: {qtd8} candidato(s)")
print(f"Nota 9: {qtd9} candidato(s)")
print(f"Nota 10: {qtd10} candidato(s)")
