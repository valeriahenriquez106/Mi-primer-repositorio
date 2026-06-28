texto = "Hola Mundo Python"

# Pasamos todo a minúsculas para no perder las mayúsculas (como la 'H')
texto_minuscula = texto.lower()

# Empezamos el contador en cero
contador_vocales = 0

# Revisamos cada letra del texto
for letra in texto_minuscula:
    # Si la letra es una vocal, sumamos 1 al contador
    if letra in "aeiou":
        contador_vocales += 1

# Mostramos el resultado en la pantalla
print("El texto tiene", contador_vocales, "vocales.")
