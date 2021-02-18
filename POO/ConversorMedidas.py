#Programa para convertir metros a centrimetros.

class Conversor():
    def __init__(self, metros):
        self.metros = metros
        self.centrimetro = 100

    def CalcularConversion(self):
        resultado = (self.metros * self.centrimetro)
        return resultado

    def MostrarMensaje(self):
        return f"{self.metros}m equivale a {self.CalcularConversion()}cm"

metros = Conversor(int(input("Escribe la cantidad de metros: ")))
print(metros.MostrarMensaje())