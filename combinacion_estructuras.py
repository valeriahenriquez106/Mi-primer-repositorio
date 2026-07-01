inventario = {
    "producto1": {
        "nombre": "Computadora",
        "precio": 650.00,
        "categorias": ("Electrónica", "Oficina", "Tecnología")
    },
    "producto2": {
        "nombre": "Mochila",
        "precio": 35.00,
        "categorias": ("Accesorios", "Escolar")
    }
}

lista_productos = list(inventario.values())

print("Información completa del inventario:")
print(lista_productos)
