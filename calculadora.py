num1 = 10
num2 = 5
operador = "+"

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: No se puede dividir entre cero"
else:
    resultado = "Operador no válido"

print(resultado)
