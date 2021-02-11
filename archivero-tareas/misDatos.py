def misDatos():
    preguntas = ["Nombre", "Apellido", "Edad", "Tarjeta de Identidad"]
    respuestas = ["Brian", "Castro", "16", "1098306124"]
    for pregunta, respuesta in zip(preguntas, respuestas):
        print(f"¿Cual es tu {pregunta}? La respuesta es: {respuesta}")
misDatos()