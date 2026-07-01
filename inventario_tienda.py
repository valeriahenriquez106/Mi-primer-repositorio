inventario = {
    "Laptop": [(850.00, 4)],
    "Mouse": [(25.00, 15)],
    "Teclado": [(45.00, 3)],
    "Monitor": [(175.00, 8)],
    "Audífonos": [(60.00, 2)]
}

valor_total = 0.0
bajo_stock = []

for producto, datos in inventario.items():
    precio, stock = datos[0]
    
    valor_total += precio * stock
    
    if stock < 5:
        bajo_stock.append(producto)

print("Valor total del inventario: $" + str(valor_total))
print("Productos con bajo stock (menos de 5 unidades):", bajo_stock)
