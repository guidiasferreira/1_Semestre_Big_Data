
notas = [[5], [3], [4], [1]]

cont = 0
soma = 0

for i in range(len(notas)):
    for j in range(len(notas[i])):
        soma = soma + notas [i] [j]
        cont = cont + 1
        
media = soma / cont
print(f"A soma das notas = {soma}\nMédia = {media}")