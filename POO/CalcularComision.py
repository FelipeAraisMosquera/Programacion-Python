#Programa que permite calcular la comision de un empleado.

class Comision():
    def __init__(self, valorContrato: float):
        #Definiendo propiedades de la clase
        self.valorContrato: float = valorContrato
        self.comision: float = 0.10

    #Creando los metodos de la clase
    def __CalcularComision(self):
        resultadoComision: float = (self.valorContrato * self.comision) / 100
        return resultadoComision

    def MostrarComision(self):
        return f"Hola! Su comision es de el {self.__CalcularComision()}%"

contrato = Comision(float(input("Escribe el valor del contrato: ")))
print(contrato.MostrarComision())