# -----------------------------------------------
# Generador de Tabla de Verdad en Python
# Autor: Sebastián Marcelo Sariella
# Descripción: Este programa permite generar tablas de verdad
# para operaciones lógicas básicas (AND, OR, NOT).
# El usuario puede elegir la operación y repetir el proceso
# hasta que decida salir.
# -----------------------------------------------

# Mensaje de bienvenida y opciones disponibles
print("Bienvenido al Generador de Tabla de Verdad")
print("Operaciones disponibles: AND, OR, NOT")
print("Escriba 'SALIR' para terminar el programa.\n")

# Lista con los posibles valores booleanos
valores = [0, 1]

# Bucle principal: se repite hasta que el usuario escriba 'SALIR'
while True:
    # Solicita al usuario la operación lógica deseada
    operacion = input("Ingrese la operación lógica que desea usar: ").upper()

    # Condición de salida del programa
    if operacion == "SALIR":
        print("Gracias por usar el generador. ¡Hasta la próxima!")
        break

    # Generación de la tabla de verdad según la operación seleccionada
    print("\nTabla de Verdad:")

    # Operación NOT: solo necesita una variable (A)
    if operacion == "NOT":
        print("A | NOT A")
        for A in valores:
            # NOT invierte el valor: 0 → 1, 1 → 0
            resultado = 1 if A == 0 else 0
            print(f"{A} |   {resultado}")

    # Operación AND: requiere dos variables (A y B)
    elif operacion == "AND":
        print("A | B | A AND B")
        for A in valores:
            for B in valores:
                # AND solo da 1 si ambos son 1
                resultado = 1 if A == 1 and B == 1 else 0
                print(f"{A} | {B} |    {resultado}")

    # Operación OR: requiere dos variables (A y B)
    elif operacion == "OR":
        print("A | B | A OR B")
        for A in valores:
            for B in valores:
                # OR da 1 si al menos uno es 1
                resultado = 1 if A == 1 or B == 1 else 0
                print(f"{A} | {B} |   {resultado}")

    # Si la operación ingresada no es válida
    else:
        print("Operación no válida. Intente con AND, OR, NOT o SALIR.")

    # Separador visual entre ejecuciones
    print("\n----------------------------------\n")
