# Generador de tabla de verdad con repetición
print("Bienvenido al Generador de Tabla de Verdad")
print("Operaciones disponibles: AND, OR, NOT")
print("Escriba 'SALIR' para terminar el programa.\n")

valores = [0, 1]

while True:
    operacion = input("Ingrese la operación lógica que desea usar: ").upper()

    if operacion == "SALIR":
        print("Gracias por usar el generador. ¡Hasta la próxima!")
        break

    print("\nTabla de Verdad:")
    if operacion == "NOT":
        print("A | NOT A")
        for A in valores:
            resultado = 1 if A == 0 else 0
            print(f"{A} |   {resultado}")
    elif operacion == "AND":
        print("A | B | A AND B")
        for A in valores:
            for B in valores:
                resultado = 1 if A == 1 and B == 1 else 0
                print(f"{A} | {B} |    {resultado}")
    elif operacion == "OR":
        print("A | B | A OR B")
        for A in valores:
            for B in valores:
                resultado = 1 if A == 1 or B == 1 else 0
                print(f"{A} | {B} |   {resultado}")
    else:
        print("Operación no válida. Intente con AND, OR, NOT o SALIR.")

    print("\n----------------------------------\n")