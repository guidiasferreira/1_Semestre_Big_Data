
n1 = int(input("Entre com o 1º número: "))
n2 = int(input("Entre com o 2º número: "))

res1 = (n1 > n2)
res2 = (n1 < n2)
res3 = (n1 == n2)
res4 = (n1 != n2)

print(f"{n1} > {n2} = {res1}")
print(f"{n1} < {n2} = {res2}")
print(f"{n1} == {n2} = {res3}")
print(f"{n1} != {n2} = {res4}") 

print(f" {n1} > {n2} = {res1} \n {n1} < {n2} = {res2} \n {n1} == {n2} = {res3} \n {n1} != {n2} = {res4}")