#Trabajo con archivos y ficheros.
def escribir(nombre: str):
    ruta = "fichero.txt"
    with open(ruta, mode='a+', encoding='utf-8') as fichero:
        fichero.write(f"Nombre: {nombre}")
        fichero.close()

def leer():
    ruta = "fichero.txt"
    with open(ruta, mode='r') as fichero:
        contenido = fichero.read()
        print(contenido)
        fichero.close()

escribir(input("Escribe tu nombre: "))
leer()