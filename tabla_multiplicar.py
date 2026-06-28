tabla_del = int(input("¿De qué número quieres la tabla de multiplicar?: "))

print(f"--- TABLA DEL {tabla_del} ---")

for contador in range(1, 11):
    resultado = tabla_del * contador
    print(f"{tabla_del} x {contador} = {resultado}")
