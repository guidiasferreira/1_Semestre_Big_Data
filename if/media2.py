
p1 = float(input("Digite a primeira nota: "))
p2 = float(input("Digite a segunda nota: "))
p3 = float(input("Digite a terceira nota: "))

media = (p1 + p2 + p3) / 3

if media >= 6:
    print(f"Aluno aprovado com média = {media :.1f}")
    
elif media >= 4:
    print(f"Aluno de recuperação = {media :.1f}")
    
else:
    print(f"Aluno reprovado com média = {media :.1f}")