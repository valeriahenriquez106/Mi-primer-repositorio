filas = 4

for i in range(1, filas + 1):
    espacios = " " * (filas - i)
    
    subida = ""
    for j in range(1, i + 1):
        subida += str(j)
        
    bajada = ""
    for j in range(i - 1, 0, -1):
        bajada += str(j)
        
    print(espacios + subida + bajada)
