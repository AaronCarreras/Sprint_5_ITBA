class Clientes():

    def __init__(self, nombre, apellido, numero_cliente, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cliente = numero_cliente
        self.dni = dni

    def __str__(self):

        print(f"Nombre: {self.nombre} \n Apellido: {self.apellido} \
        \n Numero: {self.numero_cliente} \n DNI: {self.dni}")

class Classic(Clientes):

    def __init__(self, nombre, apellido, numero_cliente, dni):

        super().__init__(nombre, apellido, numero_cliente, dni)

        self.tipo = "Classic"
        self.ca_pesos = 1
        self.ca_dolar = "N/A"
        self.cc = "N/A"
        self.tarjeta_debito = 1
        self.tarjeta_credito = "N/A"
        self.chequera = "N/A"
        self.dolar_compra_venta = False
        self.retiro_max = 10_000
        self.limit_transf = 150_000
        self.com_transaccion = 0.01

    def __str__(self):

        super().__str__()

        print(f"Tipo: {self.tipo}\n CA_Pesos: {self.ca_pesos}\n CA_Dolar: {self.ca_dolar}\
        \n CC: {self.cc}\n Tarjeta de Debito: {self.tarjeta_debito}\n Tarjeta de Credito: {self.tarjeta_credito}\
        \n Chequera:{self.chequera}\n Compra/Venta Dolar: {self.dolar_compra_venta}\n Retiro Max: {self.retiro_max}\
        \n Comision por Transaccion: {self.com_transaccion}\n Limite de Transferencia: {self.limit_transf}")

class Gold(Clientes):

    def __init__(self, nombre, apellido, numero_cliente, dni):

        super().__init__(nombre, apellido, numero_cliente, dni)

        self.tipo = "Gold"
        self.ca_pesos = 1
        self.ca_dolar = 1
        self.cc = 1
        self.tarjeta_debito = 1
        self.chequera = 1
        self.tarjeta_credito = 1
        self.dolar_compra_venta = True
        self.retiro_max = 20_000
        self.limit_transf = 500_000
        self.com_transaccion = 0.005
        self.monto_descubierto = 10_000

    def __str__(self):

        super().__str__()

        print(f"Tipo: {self.tipo}\n CA_Pesos: {self.ca_pesos}\n CA_Dolar: {self.ca_dolar}\
        \n CC: {self.cc}\n Tarjeta de Debito: {self.tarjeta_debito}\n Tarjeta de Credito: {self.tarjeta_credito}\
        \n Chequera:{self.chequera}\n Compra/Venta Dolar: {self.dolar_compra_venta}\n Retiro Max: {self.retiro_max}\
        \n Comision por Transaccion: {self.com_transaccion}\n Limite de Transferencia: {self.limit_transf}\
        \n Monto Descubierto: {self.monto_descubierto}")

class Black(Clientes):

    def __init__(self, nombre, apellido, numero_cliente, dni):

        super().__init__(nombre, apellido, numero_cliente, dni)

        self.tipo = "Black"
        self.ca_pesos = 1
        self.ca_dolar = 1
        self.cc = 1
        self.tarjeta_debito = 1
        self.chequera = 2
        self.tarjeta_credito = 5
        self.dolar_compra_venta = True
        self.retiro_max = 100_000
        self.limit_transf = 500_000
        self.com_transaccion = "N/A"
        self.monto_descubierto = 10_000

    def __str__(self):

        super().__str__()

        print(f"Tipo: {self.tipo}\n CA_Pesos: {self.ca_pesos}\n CA_Dolar: {self.ca_dolar}\
        \n CC: {self.cc}\n Tarjeta de Debito: {self.tarjeta_debito}\n Tarjeta de Credito: {self.tarjeta_credito}\
        \n Chequera:{self.chequera}\n Compra/Venta Dolar: {self.dolar_compra_venta}\n Retiro Max: {self.retiro_max}\
        \n Comision por Transaccion: {self.com_transaccion}\n Limite de Transferencia: {self.limit_transf}\
        \n Monto Descubierto: {self.monto_descubierto}")
