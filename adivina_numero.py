import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("¡Bienvenido al juego! He pensado un número entre 1 y 100.")

while True:
    intento_usuario = int(input("Introduce tu número: "))
    intentos += 1
    
    if intento_usuario == numero_secreto:
        print("¡Felicidades! Adivinaste el número en " + str(intentos) + " intentos.")
        break
    elif intento_usuario < numero_secreto:
        print("Muy bajo. Intenta de nuevo.")
    else:
        print("Muy alto. Intenta de nuevo.")
