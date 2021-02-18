#Programa para calculo de tamales.

class Tamales():
    def __init__(self, cantidadTamales, numeroBolsas):
        #Definicion de propiedades.
        self.cantidad = cantidadTamales
        self.bolsas = numeroBolsas
        self.precio = 7000
        self.precioBolsas = 100
        self.domicilio = 3000

    def Costo(self):
        costoTotal = (self.cantidad * self.precio) + (self.bolsas * self.precioBolsas) + self.domicilio
        return costoTotal
    
    def MostrarEnvio(self):
        return f"El costo total del envio es {self.Costo()}"
    
    def MostrarCantBolsas(self):
        return f"El numero total de bolsas es {self.bolsas}"

restaurante = Tamales(int(input("Cantidad de tamales: ")), int(input("Numero de bolsas: ")))
print(restaurante.MostrarEnvio())