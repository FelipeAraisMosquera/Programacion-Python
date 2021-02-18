#Programa que convierte dolares a pesos.

class Convertor():
    def __init__(self, dolares):
        #definicion de propiedades de clase.
        self.dolares = dolares
        self.costoDolar = 3600
    
    def ConvertirPesos(self):
        resultado = self.dolares * self.costoDolar
        return resultado
    
    def MostrarMensaje(self):
        return f"{self.dolares} es equivalente a {self.ConvertirPesos()} pesos"

moneda = Convertor(float(input("Escribe el monto en dolares: ")))
print(moneda.MostrarMensaje())