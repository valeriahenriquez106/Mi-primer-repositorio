lado1, lado2, lado3 = 5, 5, 5

es_valido = (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

if es_valido:
    if lado1 == lado2 == lado3:
        print("Es un triángulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Es un triángulo isósceles.")
    else:
        print("Es un triángulo escaleno.")
else:
    print("Las medidas no forman un triángulo válido.")
