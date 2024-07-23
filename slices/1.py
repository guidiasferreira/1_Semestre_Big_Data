
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = lista [:]

for i in a:
    print(i, " ", sep = " ", end = " ")
print("\n")

b = lista [:7]

for i in b:
    print(i, " ", sep = " ", end = " ")
print("\n")

c = lista [1: 8: 2]

for i in c:
    print(i, " ", sep = "", end = "")
print("\n") 

