texto = "hola mundo hola python mundo mundo"

palabras = texto.split()
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Frecuencia de palabras:", frecuencia)
