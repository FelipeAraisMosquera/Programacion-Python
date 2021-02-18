#Programa que calcula el total de compra de hamburguesas.

class Hamburguesa():
    def __init__(self, cantidad: int, productoAdicional: int):
        self.cantidad: int = cantidad
        self.costo = 7000
        self.envio = 3000
        self.adicional = productoAdicional
        self.costoAdicional = 1000
    
    def CalcularTotal(self):
        resultado = (self.cantidad * self.costo) + self.envio + (self.adicional * self.costoAdicional)
        return resultado
    
    def MostrarMensaje(self):
        return f"El total de su compra es {self.CalcularTotal()}"

hamburguesa = Hamburguesa(int(input("Escribe la cantidad de hamburguesas: ")), int(input("Cantidad de productos adicionales: ")))
print(hamburguesa.MostrarMensaje())