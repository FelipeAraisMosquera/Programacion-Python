class Sumatoria:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def sumar(self):
        return self.num1 + self.num2          

suma = Sumatoria(float(input("Numero 1: ")), float(input("Numero 2: ")))
print(f"El resultado de la suma de Num1 + Num2 es: {suma.sumar()}")