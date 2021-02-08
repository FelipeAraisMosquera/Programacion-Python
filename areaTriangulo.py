def areaTriangulo(base, altura):
    result: float = base * altura / 2
    print(f"El area del triangulo es: {result}")
areaTriangulo(float(input("Base del triangulo: ")), float(input("Altura del triangulo: ")))