""" Realizar una agenda, donde se pregunte nombre, direccion, no. telefono. Insertar
datos y guardarlos en un archivo de texto """

def miAgenda(nombre, direccion, celular: int):
    datos = nombre, direccion, celular
    agenda = open("Agenda.txt", "a+")
    agenda.write(f"Agenda de Contactos {datos}\n")
    for dato in agenda:
        agenda.read(dato)
    agenda.close()
#miAgenda(input("Escribe tu nombre: "), input("Escribe tu direccion: "), int(input("Digita tu No. Telefonico: ")))

def AgregarAgenda(nombre, direccion, telefono: int):
    route: str = "agenda.txt"
    with open(route, mode='a+', encoding="utf-8") as ficheroAgenda:
        ficheroAgenda.write("\n Agenda de Contactos \n")
        ficheroAgenda.write(f"Nombre: {nombre} \n")
        ficheroAgenda.write(f"Direccion: {direccion} \n")
        ficheroAgenda.write(f"Telefono: {telefono} \n")
        ficheroAgenda.close()

def MostrarAgenda():
    route: str = "agenda.txt"
    with open(route, mode='r') as ficheroAgenda:
        contenido = ficheroAgenda.read()
        print(contenido)
        ficheroAgenda.close()

AgregarAgenda(input("Escribe tu nombre: "), input("Escribe tu direccion: "), int(input("Digita tu No. Telefonico: ")))
MostrarAgenda()