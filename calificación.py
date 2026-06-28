calificacion = 85
if calificacion >= 90:
    letra = "A"
elif calificacion >= 80:
    letra = "B"
elif calificacion >= 70:
    letra = "C"
elif calificacion >= 60:
    letra = "D"
else:
    letra = "F"

print(f"La calificación {calificacion} equivale a una: {letra}")
