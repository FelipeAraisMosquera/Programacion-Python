#Listas y tipos de datos en las listas.
listInts = [1, 2, 3]
string_Lista = ["A", "B", "C"]
lista_vacia = []
lista_mezclada = [1, "A", 3.1416, True, None]
print(type(lista_mezclada))
lista_multiple = [['a', 'b', 'c'], [1, 2, 3]]

print(lista_multiple[0])

#Nombres en lista
names = ["Brian", "Santiago", "Marlon", "Pepe", "Sofia"]
print(names[0]) #Brian
print(names[1]) #Santiago
print(names[-2]) #Pepe
print(names[-1]) #Sofia

names.append("Teresa") #Inserta el nombre al final

names.insert(1, "Lola") #Inserta en la posicion asignada
print(names)

names.remove("Teresa")
print(names)

a = len(names) #Tamaño de la lista
print(a)

names.reverse()
print(names)

for name in names: #Recorrido de lista.
    print(name)

nums = []
for x in range(4):
    x = input("Digite un numero: ")
    nums.insert(0, x)

print(nums)

#Diccionarios.
myDic = {"Brian": "Castro", "Edad": 16, "Nacionalidad": "Colombiana"}
print(myDic)
print(myDic['Brian']) #Castro
print(myDic.keys())
print(myDic.values())

tupla = (1, 2, 3, "Brian")
tupla2 = 'Hola'
print(tupla)
print(tupla[0])
print(tupla[3] + " " + tupla2) #Concatenas tupkas.

