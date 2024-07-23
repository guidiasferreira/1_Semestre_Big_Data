
l1 = float(input("Digite o valor do primeiro lado: "))
l2 = float(input("Digite o valor do segundo lado: "))
l3 = float(input("Digite o valor do terceiro lado: "))

if (l1 < (l2 + l3)) and (l2 < (l1 + l3)) and (l3 < (l1 + l2)):
    
    if (l1 == l2) and (l2 == l3):
       print("Triângulo equilátero")
       
    elif (l1 != l2) and (l1 != l3) and (l2 != l3):
        print("Triângulo escaleno")
        
    else:
        print("Triângulo isóceles ") 
else:
    print("Não forma um triângulo")
     
print("FIM")
    