lado1 = 3
lado2 = 4
lado3 = 5

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    resultado = "Es un triángulo válido"
else:
    resultado = "No es un triángulo válido"

print(resultado)
