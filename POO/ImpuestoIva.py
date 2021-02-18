#Programa sobre el impuesto del IVA.

class Impuesto():
    def __init__(self, compra: float):
        self.precioCompra: float = compra
        self.iva: float = 0.19

    def SacarImpuesto(self):
        resultadoImpuesto = (self.precioCompra * self.iva) / 100
        return resultadoImpuesto
    
    def __str__(self):
        return f"El valor del impuesto del IVA es de {self.SacarImpuesto()}"

producto = Impuesto(float(input("Escribe el costo de la compra: ")))
print(producto.__str__())