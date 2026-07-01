import math

numero = 17

es_primo = True

if numero <= 1:
    es_primo = False
else:
    limite = int(math.sqrt(numero))
    for i in range(2, limite + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print("El número", numero, "es primo.")
else:
    print("El número", numero, "no es primo.")
