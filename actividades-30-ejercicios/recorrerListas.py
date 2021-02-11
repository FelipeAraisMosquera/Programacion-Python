def lista():
    for x in ["one", "two", "three"]:
        print(x)
lista()

def enumera():
    for index, item in enumerate(["Juan", "Pepe", "Lola", "Any"]):
        print(index, item)
enumera()

i = 0

while i < 11:
    print(i)
    i += 1
else:
    print("Done")

for i in range(2):
    print(i)
    if i == 1:
        break
else:
    print("Done")

def tuplas():
    colleccion = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    for item in colleccion:
        i1 = item[0]
        i2 = item[1]
        i3 = item[2]
        print(i1)
tuplas()