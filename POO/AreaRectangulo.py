#Programa sobre el area del rectangulo.

class Area:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def HallarArea(self):
        return self.base * self.altura

#Instanciando objeto rectangulo.
rectangulo = Area(float(input("Escribe la base: ")), float(input("Escriba la altura: ")))