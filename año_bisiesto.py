año = 2024

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    resultado = "Es bisiesto"
else:
    resultado = "No es bisiesto"

print(resultado)
