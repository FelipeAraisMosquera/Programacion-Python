#Programa para hallar area del circulo.

from math import pi

class Area():
    def __init__(self, radio: float, msj: str):
        #Deficionion de propiedades de clase
        self.radio = radio
        self.mensaje = msj

    def __MostrarArea(self):
        resultadoArea = pi * self.radio ** 2
        return resultadoArea

    def MensajeArea(self):
        return f"¡Hola! El resultado del Area del Cirulo es {self.__MostrarArea()}"
    
    def ImprimirMensaje(self):
        return f"{self.mensaje}"


circulo = Area(float(input("Escribe el radio: ")), input("Escribe un mensaje por pantalla: "))
print(circulo.MensajeArea())
print(circulo.ImprimirMensaje())