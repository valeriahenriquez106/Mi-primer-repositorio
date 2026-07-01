agenda = {}

def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print("Contacto '" + nombre + "' agregado con éxito.")

def buscar_contacto(nombre):
    if nombre in agenda:
        print("Contacto encontrado -> " + nombre + ": " + agenda[nombre])
    else:
        print("El contacto '" + nombre + "' no existe en la agenda.")

def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto '" + nombre + "' eliminado con éxito.")
    else:
        print("No se pudo eliminar: el contacto '" + nombre + "' no existe.")

agregar_contacto("Fatima", "7123-4567")
agregar_contacto("Wilfredo", "7890-1234")

buscar_contacto("Fatima")

eliminar_contacto("Wilfredo")

eliminar_contacto("Brian")
