import math

punto1 = (0, 0)
punto2 = (3, 4)

x1, y1 = punto1
x2, y2 = punto2

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La distancia entre los puntos es:", distancia)
