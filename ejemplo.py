numero = 0

def contador():
    global suma_a
    suma_a=numero+1

while True:
    contador()
    numero=suma_a
    print(numero)
    input("suma")