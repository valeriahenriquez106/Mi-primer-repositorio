import random
import string

def generar_contrasena(longitud=12):
    if longitud < 4:
        return "La longitud debe ser de al menos 4 caracteres."
        
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation
    
    # Aseguramos al menos un carácter de cada tipo para cumplir los criterios
    password = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    
    # El resto de la contraseña se llena con una mezcla de todo
    todos_los_caracteres = mayusculas + minusculas + numeros + simbolos
    for _ in range(longitud - 4):
        password.append(random.choice(todos_los_caracteres))
        
    # Mezclamos la lista por completo para que no queden en el mismo orden
    random.shuffle(password)
    
    # Unimos la lista en una sola cadena de texto
    return "".join(password)

nueva_contra = generar_contrasena(14)
print("Tu contraseña segura es:", nueva_contra)
