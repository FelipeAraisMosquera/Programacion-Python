#Programa sobre las cortinas

class Cortina():
    def __init__(self, cantidadCortinas: int):
        #Declarando propiedades de la clase.
        self.cantidad = cantidadCortinas
        self.costo: int = 120000
        self.envio: int =  20000
        self.seguro: int = 3000
    
    def CalcularCosto(self):
        self.seguro *= self.cantidad
        costoTotal = (self.cantidad * self.costo) + self.envio - self.seguro
        return costoTotal

    def MostrarMensaje(self):
        return f"La cantidad de cortinas es {self.cantidad} con un costo total de {self.CalcularCosto()}"

domicilio = Cortina(int(input("Cantidad de cortinas: ")))
print(domicilio.MostrarMensaje())