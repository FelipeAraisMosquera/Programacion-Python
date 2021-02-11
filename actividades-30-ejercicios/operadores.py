#Todo sobre operadores.
import math

a, b = 2, 3
print(a ** b) # = 8

print(pow(a, b)) # = 8

print(math.pow(a, b)) # = 8

#and
x = True
y = True
z = x and y #True
print(z)

x = False
y = True
z = x and y #False
print(z)

#Or
x = True
y = True
z = x or y #True
print(z)

x = False
y = True
z = x or y #False
print(z)