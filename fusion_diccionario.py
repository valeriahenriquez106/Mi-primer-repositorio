dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 15, "c": 25, "d": 35}

resultado = dict1.copy()

for clave, valor in dict2.items():
    if clave in resultado:
        resultado[clave] += valor
    else:
        resultado[clave] = valor

print("Diccionario fusionado:", resultado)
