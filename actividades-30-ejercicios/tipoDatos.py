#Entero
a = 5
print(a)

#Enteros
b = 96873345678
print(b)

#Float.
pi = 3.1416
print(type(pi))

#String
c = 'C'
print(c)

#String
nombre = "Brian Castro"
print(nombre)

#Bool
esBooleano = True
print(esBooleano)

#None
x = None
print(x)

#Asignacion multiple
a, b, c = 1, 2, 3
print(a, b, c)

a = b = c = 1
print(a, b, c)

#Salida de listas
x = [1, 2, [3, 4, 5], 6, 7] #lista
print(x[2])
print(x[2][1])
#salida: 4

#Tema de identacion.
a = 3
b = 4
if a > b:
    print(a)
else:
    print(b)

def my_function():
    a = 2
    return a

print(my_function())