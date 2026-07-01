jugador1 = "piedra"
jugador2 = "tijeras"

opciones_validas = ["piedra", "papel", "tijeras"]

if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
    print("Error: Una de las opciones ingresadas no es válida.")
elif jugador1 == jugador2:
    print("¡Es un empate!")
elif (jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijeras" and jugador2 == "papel"):
    print("¡Gana el Jugador 1!")
else:
    print("¡Gana el Jugador 2!")
