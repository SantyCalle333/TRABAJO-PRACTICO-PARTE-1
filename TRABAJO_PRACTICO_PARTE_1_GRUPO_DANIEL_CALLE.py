import datetime

class Usuario:
    def __init__(self, nombre, edad, num_cedula, num_celular, correo, datos_faciales, huella_dactilar):
        self.nombre = nombre
        self.edad = edad
        self.num_cedula = num_cedula
        self.num_celular = num_celular
        self.correo = correo
        self.datos_faciales = datos_faciales
        self.huella_dactilar = huella_dactilar
        self.pagos_realizados = []  # Lista para almacenar los datos de pago

    def registrar_pago(self, fecha, monto):
        pago = {"fecha": fecha, "monto": monto}
        self.pagos_realizados.append(pago)

class Acudiente(Usuario):
    def __init__(self, nombre, edad, num_identidad, datos_faciales, huella_dactilar):
        super().__init__(nombre, edad, num_identidad, None, None, datos_faciales, huella_dactilar)

class CuentaBancaria:
    def __init__(self, tipo_banco, num_cuenta, titular, tipo_cuenta):
        self.tipo_banco = tipo_banco
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.tipo_cuenta = tipo_cuenta

class Membresia:
    def __init__(self, usuario, fecha_inicio, costo):
        self.usuario = usuario
        self.fecha_inicio = fecha_inicio
        self.costo = costo

    def cobrar_membresia(self):
        if datetime.datetime.now().date() == self.fecha_inicio:
            if self.usuario.pagos_realizados:
                print("El usuario ha realizado pagos previos.")
            else:
                print("El usuario no ha realizado pagos previos.")

# Ejemplo de uso:
usuario1 = Usuario("Juan Perez", 25, "123456789", "1234567890", "juan@example.com", "datos_faciales", "huella_dactilar")
cuenta_bancaria = CuentaBancaria("Banco X", "1234567890", "Juan Perez", "Ahorros")
usuario1.registrar_pago(datetime.date(2024, 3, 31), 50)  # Registrar el pago de la membresía
membresia_usuario1 = Membresia(usuario1, datetime.date(2024, 3, 31), 50)  # Crear membresía
membresia_usuario1.cobrar_membresia()  # Verificar si el usuario ha realizado pagos previos
