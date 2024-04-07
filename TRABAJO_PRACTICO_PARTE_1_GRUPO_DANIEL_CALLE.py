import datetime

class Usuario:
    def __init__(self, nombre, edad, num_cedula, num_celular, correo):
        self.nombre = nombre
        self.edad = edad
        self.num_cedula = num_cedula
        self.num_celular = num_celular
        self.correo = correo
        self.pagos_realizados = []  # Lista para almacenar los datos de pago

    def registrar_pago(self, fecha, monto):
        pago = {"fecha": fecha, "monto": monto}
        self.pagos_realizados.append(pago)

class Invitados:
    def __init__(self, nombre, edad, num_cedula, num_celular, correo):
        self.nombre = nombre
        self.edad = edad
        self.num_cedula = num_cedula
        self.num_celular = num_celular
        self.correo = correo

class Acudiente(Usuario):
    def __init__(self, nombre, edad, num_identidad, correo):
        super().__init__(nombre, edad, num_identidad, None, correo)

class acceso_invitados(Invitados):
    def __init__(self, nombre, edad, num_identidad, correo):
        super().__init__(nombre, edad, num_identidad, None, correo)
        
class Datafono:
    def __init__(self, tipo_banco, num_cuenta, titular, tipo_cuenta):
        self.tipo_banco = tipo_banco
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.tipo_cuenta = tipo_cuenta

class Membresia_Premium:
    def __init__(self, usuario, fecha_inicio, costo, acceso_invitados):
        self.usuario = usuario
        self.fecha_inicio = fecha_inicio
        self.costo = costo
        self.acceso_invitados = acceso_invitados
        self.pagos_realizados = []

    def cobrar_membresia(self):
        fecha_actual = datetime.datetime.now().date()
        if fecha_actual.day == self.fecha_inicio.day:
            if not self.usuario.pagos_realizados or self._ultimo_pago_mes_anterior():
                self.usuario.registrar_pago(fecha_actual, self.costo)
                print(f"Se ha cobrado la membresía de {self.costo} el {fecha_actual}")
            else:
                print("El usuario ya ha realizado el pago este mes.")
        else:
            print("Hoy no es el día de cobro de la membresía.")

    def _ultimo_pago_mes_anterior(self):
        fecha_mes_anterior = datetime.datetime.now().date() - datetime.timedelta(days=30) # Considerando meses de 30 días
        for pago in self.usuario.pagos_realizados:
            if pago["fecha"].month == fecha_mes_anterior.month and pago["fecha"].year == fecha_mes_anterior.year:
                return True
        return False


# Ejemplo de uso:
usuario1 = Usuario("Juan Perez", 25, "123456789", "1234567890", "juan@example.com")
Datafono = Datafono("Banco X", "1234567890", "Juan Perez", "Ahorros")
acceso_invitados1 = acceso_invitados("Invitado1", 20, "987654321", "0987654321")
membresia_usuario1 = Membresia_Premium(usuario1, datetime.date(2024, 4, 6), 50, None)  # Crear membresía premium
usuario1.registrar_pago(datetime.date(2024, 4, 6), 50)  # Registrar el pago de la membresía
membresia_usuario1.cobrar_membresia()  # Verificar si el usuario ha realizado pagos previos

# Simulación de cobro de membresía cada mes
for _ in range(0):
    membresia_usuario1.cobrar_membresia()