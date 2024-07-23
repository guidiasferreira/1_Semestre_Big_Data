
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x2 = [a ** 2 for a in lista1 if a % 2 == 0 and a % 5 == 0]
print(x2)

lista2 = lista1 [:]

x3 = [b ** 2 for b in lista2 if b % 2 == 0 or b % 5 == 0]
print(x3)