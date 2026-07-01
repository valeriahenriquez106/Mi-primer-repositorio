banco = {
    "001": {"titular": "Vale", "saldo": 500.00, "tipo": "Ahorros", "historial": []},
    "002": {"titular": "Fatima", "saldo": 150.00, "tipo": "Corriente", "historial": []},
    "003": {"titular": "Wilfredo", "saldo": 50.00, "tipo": "Ahorros", "historial": []}
}

def depositar(num_cuenta, monto):
    if num_cuenta in banco and monto > 0:
        banco[num_cuenta]["saldo"] += monto
        # Guardamos en el historial una tupla: (Tipo_Movimiento, Monto)
        banco[num_cuenta]["historial"].append(("Depósito", monto))
        print("Depósito de $" + str(monto) + " exitoso en la cuenta " + num_cuenta)
    else:
        print("Error: Cuenta no existe o monto inválido.")

def retirar(num_cuenta, monto):
    if num_cuenta in banco:
        saldo_actual = banco[num_cuenta]["saldo"]
        if monto <= saldo_actual and monto > 0:
            banco[num_cuenta]["saldo"] -= monto
            banco[num_cuenta]["historial"].append(("Retiro", monto))
            print("Retiro de $" + str(monto) + " exitoso de la cuenta " + num_cuenta)
        else:
            print("Error: Fondos insuficientes. No se permiten saldos negativos.")
    else:
        print("Error: Cuenta no existe.")

def transferir(origen, destino, monto):
    if origen in banco and destino in banco:
        saldo_origen = banco[origen]["saldo"]
        if monto <= saldo_origen and monto > 0:
            banco[origen]["saldo"] -= monto
            banco[destino]["saldo"] += monto
            
            # Registramos el movimiento en los dos historiales
            banco[origen]["historial"].append(("Transferencia Enviada a " + destino, monto))
            banco[destino]["historial"].append(("Transferencia Recibida de " + origen, monto))
            print("Transferencia de $" + str(monto) + " de " + origen + " a " + destino + " exitosa.")
        else:
            print("Error: Fondos insuficientes en la cuenta de origen.")
    else:
        print("Error: Una o ambas cuentas no existen.")

def mostrar_estado(num_cuenta):
    if num_cuenta in banco:
        cuenta = banco[num_cuenta]
        print("\n--- ESTADO DE CUENTA " + num_cuenta + " ---")
        print("Titular: " + cuenta["titular"])
        print("Tipo   : " + cuenta["tipo"])
        print("Saldo  : $" + str(cuenta["saldo"]))
        print("Historial de Transacciones:")
        if not cuenta["historial"]:
            print("  Sin movimientos")
        for movimiento, monto in cuenta["historial"]:
            print("  - " + movimiento + ": $" + str(monto))
        print("---------------------------------")

depositar("001", 100.00)

retirar("003", 60.00)

transferir("001", "002", 200.00)

mostrar_estado("001")
mostrar_estado("002")
