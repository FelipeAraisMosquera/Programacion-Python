def teclas():
    nombre = input("¿Como es su nombre?: ")
    print(f"Un gusto conocerlo, {nombre}")
teclas()

def conversion():
    dolares = float(input("¿Cantidad de dolares?: "))
    print(f"{dolares} equivalen a {round(dolares * 3600.00)} pesos")
conversion()

def MostrarEdad():
    edad: int = int(input("Inserte su edad: "))
    print(f"Usted tiene {edad} años")
MostrarEdad()

#Resta
def Resta(a: float, b: float):
    return a - b
print(Resta(float(input("Ingrese un valor: ")), float(input("Ingrese un valor mayor: "))))