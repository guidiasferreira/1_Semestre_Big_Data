
def soma (* valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}")

soma(10, 28)
soma(8, 7)