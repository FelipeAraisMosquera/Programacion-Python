class Notas():
    def __init__(self, nota):
        self.nota = nota
    
    def CalcularPromedio(self):
        if self.nota > 3.2:
            return f"Aprobo el curso"
        elif self.nota < 3.2:
            return f"Ha desaprobado el curso"
        elif self.nota > 5.0:
            return f"La nota se pasa del promedio"
        else:
            return f"Ha introducido una nota invalida"

estudiante = Notas(float(input("Por favor inserte una nota entre 0 y 5.0: ")))
print(estudiante.CalcularPromedio())