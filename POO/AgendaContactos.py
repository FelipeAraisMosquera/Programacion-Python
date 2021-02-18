from os import remove

class Agenda:
    def __init__(self):
        #Declarando propiedades de la clase Agenda
        self.nombre = ""
        self.direccion = ""
        self.telefono: int = 0
        self.route: str = "Agenda-Contactos.txt"

    #Declaracion de metodos.
    def Main(self):
        menu = ("\n Menu de opciones \n", "1. Insertar Datos \n", "2. Mostrar Datos \n", "3. Eliminar Agenda \n", "4. Salir \n")
        for opciones in menu:
            print(opciones)
            try:
                opcion: int = int(input("Por favor, digite una opcion (1. Insertar, 2. Mostrar, 3. Eliminar Agenda, 4. Salir): "))
            except:
                print("Ha ocurrido un error")
            if opcion == 1:
                self.__AgregarAgenda(input("Escribe tu nombre: "), input("Escribe tu direccion: "), int(input("Digita tu No. Telefonico: ")))
            elif opcion == 2:
                self.__MostrarAgenda()
            elif opcion == 3:
                print("El fichero de la agenda ha sido eliminado")
                self.__EliminarAgenda()
            elif opcion == 4:
                break
            else:
                print("No escribio una opcion valida")

    def __AgregarAgenda(self, nombre, direccion, telefono: int):
        with open(self.route, mode="a+", encoding="utf-8") as fichero:
            fichero.write("\nAgenda de Contactos \n")
            fichero.write(f"Nombre del contacto: {nombre}\n")
            fichero.write(f"Direccion del contacto: {direccion}\n")
            fichero.write(f"Telefono del contacto: {telefono}\n")
            fichero.close()

    def __MostrarAgenda(self):
        with open(self.route, mode="r") as fichero:
            contenido = fichero.read()
            print(contenido)
            fichero.close()

    def __EliminarAgenda(self):
        return remove(self.route)

#Instanciando objeto.
agenda = Agenda()
agenda.Main()
#agenda._EliminarAgenda()