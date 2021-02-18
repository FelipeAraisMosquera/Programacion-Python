class Numero():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def PromediarNumeros(self):
        if self.num1 > self.num2:
            return f"El numero {self.num1} es mayor que el numero {self.num2}"
        elif self.num2 > self.num1:
            return f"El numero {self.num2} es mayor que el numero {self.num1}"
        elif self.num1 == self.num2:
            return f"Los numeros son iguales"
        else:
            return f"Los numeros no son validos"

numeros = Numero(int(input("Escribe el numero 1: ")), int(input("Escribe el numero 2: ")))
print(numeros.PromediarNumeros())