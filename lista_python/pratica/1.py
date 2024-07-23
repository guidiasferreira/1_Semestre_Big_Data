
num = [2, 5, 9, 1]
num [2] = 3
print(num)

num.append(7)
num.sort(reverse = True)
num.insert(2, 2)
num.remove(2)

if 4 in num:
    num.remove(4)

else:
    print(f"Não existe número 4")

if 5 in num:
    num.remove(5)

else:
    print(f"Não existe número 5")

print(num)
print(f"Essa lista tem {len(num)} elementos")