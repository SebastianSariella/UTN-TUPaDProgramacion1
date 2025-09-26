# Biblioteca UTN – Programación I

titulos = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
ejemplares = [5, 3, 7]

while True:
    print("""
    ===== Menú Principal =====
    1. Ingresar títulos
    2. Ingresar ejemplares
    3. Mostrar catálogo
    4. Consultar disponibilidad
    5. Listar agotados
    6. Agregar título
    7. Actualizar ejemplares (préstamo/devolución)
    8. Salir
    """)
    opcion = input("Elige una opción (1-8): ")

    if opcion == "1":
        cantidad_str = input("¿Cuántos títulos vas a ingresar? ")
        if not cantidad_str.isdigit() or int(cantidad_str) <= 0:
            print("Debes ingresar un entero mayor que cero.")
        else:
            cantidad = int(cantidad_str)
            ingresados = 0
            while ingresados < cantidad:
                titulo = input(f"Título #{ingresados+1}: ")
                while titulo == "":
                    print("El título no puede estar vacío.")
                    titulo = input(f"Título #{ingresados+1}: ")
                # Evitar duplicados (case-insensitive)
                duplicado = False
                for t in titulos:
                    if t.lower() == titulo.lower():
                        duplicado = True
                        break
                if duplicado:
                    print("Ese título ya existe en el catálogo.")
                    continue
                titulos.append(titulo)
                ejemplares.append(0)
                ingresados += 1
            print(f"{cantidad} título(s) agregado(s).")

    elif opcion == "2":
        if len(titulos) == 0:
            print("No hay títulos registrados.")
        else:
            for i in range(len(titulos)):
                numero = input("Ejemplares de '" + titulos[i] + "': ")
                while not numero.isdigit():
                    print("Debes ingresar un número entero (>= 0).")
                    numero = input("Ejemplares de '" + titulos[i] + "': ")
                ejemplares[i] = int(numero)
            print("Stock inicial actualizado.")

    elif opcion == "3":
        if len(titulos) == 0:
            print("El catálogo está vacío.")
        else:
            print("Catálogo completo:")
            for i in range(len(titulos)):
                print(str(i+1) + ". " + titulos[i] + " — " +
                      str(ejemplares[i]) + " ejemplar(es)")

    elif opcion == "4":
        if len(titulos) == 0:
            print("El catálogo está vacío.")
        else:
            buscado = input("Título a consultar: ")
            encontrado = False
            for i in range(len(titulos)):
                if buscado.lower() == titulos[i].lower():
                    print("'" + titulos[i] + "' tiene " +
                          str(ejemplares[i]) + " ejemplar(es).")
                    encontrado = True
                    break
            if not encontrado:
                print("Título no encontrado.")

    elif opcion == "5":
        agotados = []
        for i in range(len(titulos)):
            if ejemplares[i] == 0:
                agotados.append(titulos[i])
        if len(agotados) == 0:
            print("No hay libros agotados.")
        else:
            print("Libros agotados:")
            for t in agotados:
                print("- " + t)

    elif opcion == "6":
        titulo = input("Nuevo título: ")
        while titulo == "":
            print("El título no puede estar vacío.")
            titulo = input("Nuevo título: ")
        duplicado = False
        for t in titulos:
            if t.lower() == titulo.lower():
                duplicado = True
                break
        if duplicado:
            print("Ese título ya existe.")
        else:
            numero = input("Cantidad de ejemplares: ")
            while not numero.isdigit():
                print("Debes ingresar un número entero (>= 0).")
                numero = input("Cantidad de ejemplares: ")
            titulos.append(titulo)
            ejemplares.append(int(numero))
            print("'" + titulo + "' agregado con éxito.")

    elif opcion == "7":
        if len(titulos) == 0:
            print("El catálogo está vacío.")
        else:
            buscado = input("Título para actualización: ")
            idx = -1
            for i in range(len(titulos)):
                if buscado.lower() == titulos[i].lower():
                    idx = i
                    break
            if idx == -1:
                print("Título no encontrado.")
            else:
                print("1) Préstamo")
                print("2) Devolución")
                accion = input("Selecciona acción (1-2): ")
                if accion == "1":
                    if ejemplares[idx] > 0:
                        ejemplares[idx] -= 1
                        print("Préstamo exitoso.")
                    else:
                        print("No hay ejemplares disponibles.")
                elif accion == "2":
                    ejemplares[idx] += 1
                    print("Devolución exitosa.")
                else:
                    print("Opción inválida.")

    elif opcion == "8":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Ingresa un número entre 1 y 8.")


