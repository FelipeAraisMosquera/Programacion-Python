""" Realizar una agenda, donde se pregunte nombre, direccion, no. telefono. Insertar
datos y guardarlos en un archivo de texto """

""" Modificaciones:
1. Crear menu de opciones con while.
2. El programa preguntara si desea continuar o salir (1. insertar datos, 2. mostrar datos).
3. Si el usuario indica salir, se acaba el programa, en caso de que seleccione si, debe regresar y pintar
el menu para insertar y mostrar los datos.
4. Si el usuario le da insertar, llamara la funcion AgregarAgenda
5. Si el usuario le da mostrar, llamara la funcion MostrarAgenda.
"""

#Funcion principal
def Main():
    menu = ("\n Menu de opciones \n", "1. Insertar Datos \n", "2. Mostrar Datos \n", "3. Salir \n")
    for opciones in menu:
        print(opciones)
        try:
            opcion: int = int(input("Por favor, digite una opcion (1, 2, 3): "))
        except:
            print("Ha ocurrido un error")
        if opcion == 1:
            AgregarAgenda(input("Escribe tu nombre: "), input("Escribe tu direccion: "), int(input("Digita tu No. Telefonico: ")))
        elif opcion == 2:
            MostrarAgenda()
        elif opcion == 3:
            break
        else:
            print("No escribio una opcion valida")

#Funcion para agregar contactos
def AgregarAgenda(nombre, direccion, telefono: int):
    route: str = "agenda.txt"
    with open(route, mode='a+', encoding="utf-8") as ficheroAgenda:
        ficheroAgenda.write("\n Agenda de Contactos \n")
        ficheroAgenda.write(f"Nombre: {nombre} \n")
        ficheroAgenda.write(f"Direccion: {direccion} \n")
        ficheroAgenda.write(f"Telefono: {telefono} \n")
        ficheroAgenda.close()

#Funcion de mostrar contactos
def MostrarAgenda():
    route: str = "agenda.txt"
    with open(route, mode='r') as ficheroAgenda:
        contenido = ficheroAgenda.read()
        print(contenido)
        ficheroAgenda.close()

Main()