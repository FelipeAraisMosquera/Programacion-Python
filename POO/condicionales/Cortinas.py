""" Desarrolle un programa básico orientado a objetos en Python para una empresa de cortinas 
la cual necesita saber el costo total de envío de cortinas a domicilio.El costo de cada cortina 
es de 120000 Se paga $20.000 de envío Y $3000 de seguro por cada cortina.Si la cantidad de cortinas es mayor 
a 10 tienen un descuento de 200000. """

class Cortinas():
    def __init__(self, cortinas: int):
        self.costoCortina: int = 120000
        self.costoEnvio: int = 20000
        self.seguroCortina: int = 3000
        self.descuento = 200000
        self.numeroCortinas: int = cortinas

    def Main(self):
        if self.numeroCortinas <= 0:
            return f"¡No pidio una cantidad valida de cortinas!"
        print(f"1. Cantidad de Cortinas: {self.numeroCortinas}")
        print(f"2. Costo cortinas: {self.numeroCortinas * self.costoCortina}")
        print(f"3. Seguro por cada cortina: {self.numeroCortinas * self.seguroCortina}")
        print(f"4. Costo del envio: {self.costoEnvio}")
        if self.numeroCortinas > 10:
            print(f"4. Descuento: {self.descuento}")
        print(f"El costo total por las cortinas a domicilio es de ${self.__HacerCalculo()}")

    
    def __HacerCalculo(self):
        seguro = self.seguroCortina * self.numeroCortinas
        resultadoCalculo = (self.costoEnvio) + (self.costoCortina * self.numeroCortinas) + seguro
        if self.numeroCortinas > 10:
            print(f"¡Hola! Usted va a llevar {self.numeroCortinas} cortinas por lo tanto obtiene un descuento de ${self.descuento}")
            resultadoCalculo - self.descuento
        return resultadoCalculo

pedido = Cortinas(int(input("¿Cuantas cortinas desea?: ")))
pedido.Main()