registro = {
    "Fatima": {"Matemáticas": [8.5, 9.0, 9.5], "Programación": [9.0, 10.0, 9.5]},
    "Wilfredo": {"Matemáticas": [7.0, 8.0, 7.5], "Programación": [8.5, 9.0, 8.0]},
    "Brian": {"Matemáticas": [9.0, 8.5, 9.0], "Programación": [9.5, 9.5, 10.0]}
}

print("--- PROMEDIO POR ESTUDIANTE ---")
for estudiante, materias in registro.items():
    total_notas_estudiante = 0
    cantidad_notas_estudiante = 0
    
    for notas in materias.values():
        total_notas_estudiante += sum(notas)
        cantidad_notas_estudiante += len(notas)
        
    promedio_estudiante = total_notas_estudiante / cantidad_notas_estudiante
    print(estudiante + ": " + str(round(promedio_estudiante, 2)))

print("\n--- PROMEDIO POR MATERIA ---")
materias_todas = ["Matemáticas", "Programación"]

for materia in materias_todas:
    total_notas_materia = 0
    cantidad_notas_materia = 0
    
    for materias in registro.values():
        if materia in materias:
            notas = materias[materia]
            total_notas_materia += sum(notas)
            cantidad_notas_materia += len(notas)
            
    promedio_materia = total_notas_materia / cantidad_notas_materia
    print(materia + ": " + str(round(promedio_materia, 2)))
