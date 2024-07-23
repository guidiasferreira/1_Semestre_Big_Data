
n = int(input("Entre com o número de alunos: "))
cont = 1

while cont <= n:
    print(f"Dados do {cont}\u00BA aluno: ")
    nota1 = float(input("Insira o valor da primeira nota: "))
    nota2 = float(input("Insira o valor da segunda nota: "))
    nota3 = float(input("Insira o valor da terceira nota: "))
    me = float(input("Média: "))
    
    mf = (nota1 + nota2 * 2 + nota3 * 3 + me) / 7
    
    if mf >= 9.0 and mf <= 10:
        conceito = "A"
    
    elif mf >= 7.5 and mf < 9.0:
        conceito = "B"
        
    elif mf >= 6.0 and mf < 7.5:
        conceito = "C"
        
    elif mf >= 4.0 and mf < 6.0:
        conceito = "D"
        
    elif mf < 4.0:
        conceito = "E"
        
    else:
        print(f"Nota inválida!")
        
        
    print(f"Aluno = {cont}\nMédia de aproveitamento = {mf :.1f} - Conceito: {conceito}")
    
    cont = cont + 1
        