#Funciones.

def MiNumero(x):
    if x < 0:
        return "Introdujo un numero negativo"
    else:
        return x
print(MiNumero(float(input("Introduce un numero: "))))

def Func(*args):
    #Argumentos indefinidos.
    for i in *args:
        print(i)
Func(1, 2, 3)

#Funcion recursiva.
def Factorial(n):
    #n debe ser entero.
    if n == 0:
        return 1
    else:
        return n*Factorial(n-1)
print(Factorial(3))