peso = 70
altura = 1.75

imc = peso / (altura ** 2)

if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc <= 24.9:
    clasificacion = "Normal"
elif 25 <= imc <= 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print("Tu IMC es:", imc)
print("Clasificación:", clasificacion)
