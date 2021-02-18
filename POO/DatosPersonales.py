#Programa que pide los datos personales y los procese.

class Datos():
    def __init__(self, nombre, apellido, telefono, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono: int = telefono
        self.direccion = direccion
    
    def ProcesarDatos(self):
        datos = f"¡Hola {self.nombre} {self.apellido}! Sus datos fueron procesados. \n"
        return datos

    def MensajeDatos(self):
        nombre = f"Nombre de usuario: {self.nombre} \n"
        apellido = f"Apellido de Usuario: {self.apellido} \n"
        telefono = f"Telefono del usuario: {self.telefono} \n"
        direccion = f"Direccion del usuario: {self.direccion}"
        return nombre, apellido, telefono, direccion

usuario = Datos(input("Nombre: "), input("Apellido: "), int(input("Telefono: ")), input("Direccion: "))
print(usuario.ProcesarDatos())
print(usuario.MensajeDatos())