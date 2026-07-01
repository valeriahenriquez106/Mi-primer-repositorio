contrasena = "Python3.9!"

tiene_largo = len(contrasena) >= 8
tiene_mayuscula = False
tiene_numero = False
tiene_especial = False

caracteres_especiales = "!@#$%^&*(),.?\":{}|<>"

for caracter in contrasena:
    if caracter.isupper():
        tiene_mayuscula = True
    elif caracter.isdigit():
        tiene_numero = True
    elif caracter in caracteres_especiales:
        tiene_especial = True

if tiene_largo and tiene_mayuscula and tiene_numero and tiene_especial:
    print("La contraseña es segura.")
else:
    print("La contraseña no cumple con los requisitos de seguridad.")
