
peso = float(input("Digite seu peso: " ))
altura = float(input("Digite sua altura: "))
imc =  (peso / (altura**2))

if imc < 18:
    print(f"Abaixo do peso = {imc :.2f}")

elif imc >= 18 and imc <= 25:
    print(f"Peso ideal = {imc :.2f}")

elif imc >= 25 and imc <= 30:
    print(f"Acima do peso = {imc :.2f}")

else:
    print(f"Obeso = {imc :.2f}")

