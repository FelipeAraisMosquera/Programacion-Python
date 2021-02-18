#Programa que detecta si una letra es una vocal.

class Vocal():
    def __init__(self, letra):
        self.letra = letra

    def VerVocal(self):
        self.letra.upper()
        if "A" in self.letra:
            return f"En {self.letra} esta la vocal A"
        elif "E" in self.letra:
            return f"En {self.letra} esta la vocal E"
        elif "I" in self.letra:
            return f"En {self.letra} esta la vocal I"
        elif "O" in self.letra:
            return f"En {self.letra} esta la vocal O"
        elif "U" in self.letra:
            return f"En {self.letra}  esta la vocal U"
        else:
            return f"La {self.letra} no se encuentra en ninguna vocal"

letra = Vocal(input("Escribe una letra o palabra: "))
print(letra.VerVocal())