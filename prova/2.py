
n = int(input("Entre com o valor de N: "))
m = int(input("Entre com o valor de M: "))

while n <= m:
    if n % 2 == 1 and n % 3 == 0:
        print(n)
        
    n = n + 1