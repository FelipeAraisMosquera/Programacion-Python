def perimetroCuadrado(lado1, lado2, lado3, lado4):
    result: float = lado1 + lado2 + lado3 + lado4
    print(f"El resultado del perimetro del cuadrado es: {result}")
perimetroCuadrado(float(input("Lado 1: ")), float(input("Lado 2: ")), float(input("Lado 3: ")), float(input("Lado 4: ")))