from Clientes import Classic, Gold, Black
import json

file = open("JSONs/eventos_gold.json", "r")
data = json.load(file)
file.close()


if data['tipo'] == "CLASSIC":
    client = Classic(data['nombre'], data['apellido'], data['numero'], data['dni'])
elif data['tipo'] == "GOLD":
    client = Gold(data['nombre'], data['apellido'], data['numero'], data['dni'])
elif data['tipo'] == "BLACK":
    client = Black(data['nombre'], data['apellido'], data['numero'], data['dni'])
else: 
    raise ValueError("Tipo de cliente no reconocido")

for transaction in data['transacciones']:
    if transaction['estado'] == "ACEPTADA":
        print(f'''
            {transaction['tipo']} (n {transaction['numero']}): {transaction['estado']}
            Monto: {transaction['monto']}
            Fecha: {transaction['fecha']}\n
        ''')
    elif transaction['estado'] == "RECHAZADA":

        print(f'''
            {transaction['tipo']} (n {transaction['numero']}): {transaction['estado']}
            Monto: {transaction['monto']}
            Fecha: {transaction['fecha']}
            ''', end='')
        
        if transaction['tipo'] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
            if transaction['cupoDiarioRestante'] < transaction['monto']:
                print("!!! Rechazada por falta de cupo diario !!!")
            elif transaction['saldoEnCuenta'] + client.monto_descubierto < transaction['monto']:
                print("!!! Rechazada por falta de saldo en cuenta !!!")

        elif transaction['tipo'] == "ALTA_TARJETA_CREDITO":
            if client.tarjeta_credito == "N/A" or transaction['totalTarjetasDeCreditoActualmente'] <= client.tarjeta_credito:
                print("!!! Rechazada por exceder el limite de tarjetas de credito !!!")

        elif transaction['tipo'] == "ALTA_CHEQUERA":
            if client.chequera == "N/A" or transaction['totalChequerasActualmente'] <= client.chequera:
                print("!!! Rechazada por exceder el limite de chequeras !!!")
            
        elif transaction['tipo'] == "COMPRA_DOLAR":
            if not client.dolar_compra_venta:
                print("!!! Rechazada por no poner comprar dolares !!!")
            elif transaction['monto'] > transaction['saldoEnCuenta']:
                print("!!! Rechazada por falta de saldo en cuenta !!!")

        elif transaction['tipo'] == "TRANSFERENCIA_ENVIADA":
            if transaction['monto'] > transaction['saldoEnCuenta']:
                print("!!! Rechazada por falta de saldo en cuenta !!!")

        print("\n")

