#Programa que permite saber si un numero es positivo, negativo o neutro.

class Numeros():
    def __init__(self, numero):
        self.numero = numero
    
    def MostrarTipoNumero(self):
        if self.numero > 0:
            return f"El numero es positivo"
        elif self.numero < 0:
            return f"El numero es negativo"
        elif self.numero == 0:
            return f"El numero es neutro"

numero = Numeros(int(input("Escribe un numero: ")))
print(numero.MostrarTipoNumero())