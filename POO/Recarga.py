""" 
Programa de recarga que permite saber la cantidad de minutos
"""

class Recarga():
    def __init__(self, numCel, valRecarga):
        self.numCel = numCel
        self.valRecarga = valRecarga
        self.valMinuto = 100
    
    def MostrarMinutos(self):
        return self.valRecarga / self.valMinuto

    def __str__(self):
        return f"La recarga del numero: {self.numCel} ha sido exitosa!"

#Instansianciando objeto.
telefono = Recarga(int(input("Escribe el numero de celular: ")), int(input("Escribe el valor de la recarga: ")))
print(f"{telefono.__str__()} Los minutos asignados son: "
    f"{telefono.MostrarMinutos()} ")