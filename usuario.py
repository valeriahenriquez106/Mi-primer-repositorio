#Datos personales del usuario
name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
mail = input("Ingrese su correo: ")
age = input("Ingrese su edad: ")
sexo = input("Ingrese su sexo: ")
birthyear = input("Ingrese su fecha de nacimiento: ")

age = int(age)
phone = input("Ingrese su numero de telefono: ")
phone = str(phone)

#Año de nacimiento
birthyear = 2026 - age
print(f"Tu año de nacimiento es: {birthyear}") 
print(f"Nombre: {name}")
print(f"Apellido:{lastname}")
print(f"Correo: {mail}")
print(f"Edad: {age}")
print(f"Sexo: {sexo}")
print(f"Telefono: {phone}")
