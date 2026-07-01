decimal = 42

if decimal == 0:
    binario = "0"
else:
    residuos = []
    numero_trabajo = decimal
    
    while numero_trabajo > 0:
        residuo = numero_trabajo % 2
        residuos.append(str(residuo))
        numero_trabajo = numero_trabajo // 2
        
    residuos.reverse()
    binario = "".join(residuos)

print("El número", decimal, "en binario es:", binario)
