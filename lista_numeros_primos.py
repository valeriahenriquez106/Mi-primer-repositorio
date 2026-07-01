import math

inicio, fin = 10, 50

def es_primo(n):
    if n <= 1:
        return False
    limite = int(math.sqrt(n))
    for i in range(2, limite + 1):
        if n % i == 0:
            return False
    return True

primos_en_rango = []

for numero in range(inicio, fin + 1):
    if es_primo(numero):
        primos_en_rango.append(numero)

print("Números primos entre", inicio, "y", fin, ":", primos_en_rango)
