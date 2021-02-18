#Programa para jugar dados, que nos da un numero aleatorio-

from random import randrange

class Dados():
    def __init__(self, numero):
        self.num = numero
        self.aleatorio = randrange(1, 7)

    def Main(self):
        pass

    def Jugar(self):
        intentos = 5
        if self.num == self.aleatorio:
            print(f"¡Ha ganado! El numero {self.num} es el correcto.")
        while self.num != self.aleatorio: #Es igual a True
            print(f"Sigue intentando, el numero no es correcto.")
            intentos = intentos - 1
            self.num = int(input("¡Gira el dado!: "))
            print(f"Intentos: {intentos}")
            if self.num == self.aleatorio:
                print(f"¡Ha ganado! El numero {self.num} es igual a {self.aleatorio}")
            if intentos == 0:
                print(f"¡Oh vaya! Ahora tienes ({intentos}) intentos haz perdido el juego.")
                break

tirar = Dados(int(input("Escribe un numero entre 1 y 6: ")))
tirar.Jugar()