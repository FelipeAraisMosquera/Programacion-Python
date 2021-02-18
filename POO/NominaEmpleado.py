#Programa que calcula el sueldo de nomina de un empleado

class Nomina():
    def __init__(self, horasTrabajo):
        self.horas: int = horasTrabajo
        self.costoHoras: int = 15000
    
    def __CalcularNomina(self):
        resultadoCalculo = self.horas * self.costoHoras
        return resultadoCalculo

    def MensajeNomina(self, nombre: str):
        saludo = print(f"¡Hola {nombre}! Su pago de nomina es de {self.__CalcularNomina()} por las {self.horas} horas trabajadas.")

empleado = Nomina(int(input("Escribe las horas trabajadas: ")))
empleado.MensajeNomina(input("Escribe tu nombre: "))