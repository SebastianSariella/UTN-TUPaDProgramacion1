# Inicializamos el tablero vacío (3x3)
tablero = [["-" for _ in range(3)] for _ in range(3)]

# Función para mostrar el tablero
def mostrar_tablero(tablero):
    print("\nTablero actual:")
    for fila in tablero:
        print(" | ".join(fila))
    print()

# Mostrar tablero inicial
mostrar_tablero(tablero)

# Turnos alternados entre dos jugadores
for turno in range(9):  # Máximo 9 jugadas
    jugador = "X" if turno % 2 == 0 else "O"
    print(f"Turno del jugador '{jugador}'")

    while True:
        try:
            fila = int(input("Ingrese la fila (0, 1, 2): "))
            columna = int(input("Ingrese la columna (0, 1, 2): "))

            # Validar entrada
            while fila not in [0, 1, 2] or columna not in [0, 1, 2]:
                print("Fila y columna incorrecta. Intente nuevamente con 0, 1 o 2.")
                fila = int(input("Ingrese la fila (0, 1, 2): "))
                columna = int(input("Ingrese la columna (0, 1, 2): "))

            if tablero[fila][columna] == "-":
                tablero[fila][columna] = jugador
                break
            else:
                print("Esa casilla ya está ocupada. Intente otra.")
        except (ValueError, IndexError):
            print("Entrada inválida. Use números entre 0 y 2.")

    mostrar_tablero(tablero)