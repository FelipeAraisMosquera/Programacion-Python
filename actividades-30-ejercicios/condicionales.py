"""  Condicionales """

""" 
Desarrollar digiturno:
Caracteristicas:
-3 tipos de clientes; cliente general, cliente preferencial, cliente vip
-El turno se asigna de acuerdo al numero pero antes se usa la letra inicial del tipo de cliente
-Realizar un menu (con print)
-Declarar un while hasta que se oprima la tecla salir.
-Enviar por parametro el numero del menu
"""

opcion = 0
contadorpreferencial = 0
contadorgeneral = 0
contadorvip = 0


def tipocliente():
    if opcion == 1:
        print("El turno es G-" + str(contadorgeneral))
        input("presione una tecla para regresar al menu")
        
    elif opcion == 2:
        print(f"El turno es P-{contadorpreferencial}")
        input("presione una tecla para regresar al menu")

    elif opcion == 3:
        print(f"El turno es V-{contadorvip}")
        input("presione una tecla para regresar al menu")

    else:
        print("No tiene ninguna opción ")


while opcion != 4:
    print("\n Menu de opciones: \n"
          "Opcion 1: Cliente general\n"
          "Opcion 2: Cliente preferencial\n"
          "Opcion 3: Cliente vip\n"
          "Opcion 4: Salir del turno\n")
    opcion = int(input("Inserte una opcion: "))
    if opcion == 1:
        tipocliente()
        contadorgeneral += 1
    elif opcion == 2:
        tipocliente()
        contadorpreferencial += 1
    elif opcion == 3:
        tipocliente()
        contadorvip += 1
    elif opcion == 4:
        break
    else:
        print("No tiene ninguna opción")