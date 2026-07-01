numero = 1234

suma = 0
numero_trabajo = abs(numero)

while numero_trabajo > 0:
    digito = numero_trabajo % 10
    suma += digito
    numero_trabajo = numero_trabajo // 10

print("La suma de los dígitos es:", suma)
