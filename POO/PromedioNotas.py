#Programa para hayar el promedio de notas.

class Notas():
    def __init__(self, nota1: float, nota2: float, nota3: float):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def PromediarNotas(self):
        promedioTotal: float = (self.nota1 + self.nota2 + self.nota3) / 3
        return promedioTotal

promedio = Notas(float(input("Nota 1: ")), float(input("Nota 2: ")), float(input("Nota 3: ")))
print(f"El promedio de las 3 notas es {promedio.PromediarNotas()}")