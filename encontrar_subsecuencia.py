lista_principal = [1, 2, 3, 4, 5, 6]
subsecuencia = [2, 4, 6]

iterador_sub = iter(subsecuencia)
item_buscado = next(iterador_sub, None)

for numero in lista_principal:
    if numero == item_buscado:
        item_buscado = next(iterador_sub, None)

if item_buscado is None:
    print("Es una subsecuencia.")
else:
    print("No es una subsecuencia.")
