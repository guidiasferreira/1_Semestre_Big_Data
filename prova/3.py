
n = int(input("Entre com o valor de N: "))
m = int(input("Entre com o valor de M: "))
produto = 1

while n <= m:
    if n % 2 == 0:
        produto = produto * n
        
    n = n + 1
print(f"O produto é = {produto}")