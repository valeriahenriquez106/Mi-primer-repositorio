texto = "programacion en python"

frecuencias = {}

for caracter in texto:
    if caracter in frecuencias:
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1

print("Frecuencia de caracteres:", frecuencias)
