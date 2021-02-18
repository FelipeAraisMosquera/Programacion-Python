#Programa para calcular el tiempo de parqueo de una metodos

class Tiempo():
    def __init__(self, tiempo: int):
        #Declarando propiedades de la clase
        self.tiempo = tiempo
        self.costoHora = 300

    #Declarando metodos de la clase
    def TotalPago(self):
        resultado = self.tiempo * self.costoHora
        return resultado
    
    def MensajeParqueo(self):
        return f"¡Hola! Usted debe pagar un total de: {self.TotalPago()} por su parqueo."

parqueo = Tiempo(int(input("Escriba el tiempo en horas: ")))
print(parqueo.MensajeParqueo())