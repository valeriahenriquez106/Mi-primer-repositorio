texto = "Anita lava la tina"

texto_limpio = ""
for caracter in texto.lower():
    if caracter != " ":
        texto_limpio += caracter

es_palindromo = True
largo = len(texto_limpio)

for i in range(largo // 2):
    if texto_limpio[i] != texto_limpio[largo - 1 - i]:
        es_palindromo = False
        break

if es_palindromo:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
