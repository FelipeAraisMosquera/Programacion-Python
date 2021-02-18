class Semaforo():
    def __init__(self, color):
        self.color = color

    def MostrarEstado(self):
        if self.color == "Rojo":
            return f"El color esta en {self.color} tiene que parar"
        elif self.color == "Verde":
            return f"El semaforo esta en {self.color} puede continuar"
        elif self.color == "Amarillo":
            return f"El samoforo esta en {self.color} alistese"
        else:
            return f"El semaforo no tiene ese color"

semaforo = Semaforo(input("Por favor inserte el color del semaforo: "))
print(semaforo.MostrarEstado())