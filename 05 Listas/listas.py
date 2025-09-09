import random

# Ejercicio 1
notas = [7, 8.5, 6, 9, 5.5, 10, 4, 8, 7.5, 6.5]
sumatoria = 0
nota_mas_baja = notas[0]
nota_mas_alta = notas[0]
for nota in notas:
    sumatoria += nota
    # Comparamos la nota actual con la más baja y la más alta
    if nota < nota_mas_baja:
        nota_mas_baja = nota
    if nota > nota_mas_alta:
        nota_mas_alta = nota
    # Imprimimos la nota actual
    print(f"Nota: {nota}")

# Calculamos el promedio
promedio = sumatoria / len(notas)

# Imprimimos los resultados
print(f"Promedio: {promedio}")
print(f"Nota más baja: {nota_mas_baja}")
print(f"Nota más alta: {nota_mas_alta}")

# Ejercicio 2
productos = []
for i in range(5):
    nombre = input(f"Cargué el nombre del {i+1}° producto: ")
    productos.append(nombre)

# Ordenamos alfabéticamente e imprimimos
ordenados = sorted(productos)
for producto in ordenados:
    print(producto)

# Preguntamos si quiere eliminar algun producto
eliminar = input("¿Desea eliminar algún producto? (s/n): ")
if eliminar.lower() == 's':
    producto_a_eliminar = input("Ingrese el nombre del producto a eliminar: ")
    if producto_a_eliminar in productos:
        productos.remove(producto_a_eliminar)
        print(f"Producto '{producto_a_eliminar}' eliminado.")
    else:
        print(f"Producto '{producto_a_eliminar}' no encontrado en la lista.")

# Ordenamos e imprimimos la lista actualizada nuevamente
ordenados = sorted(productos)
for producto in ordenados:
    print(producto)

# Ejercicio 3
numeros = []
pares = []
impares = []
for i in range(15):
    # Incluímos el número al azar entre 1 y 100
    num = random.randint(1, 100)
    numeros.append(num)

    # Incluimos el número en la lista correspondiente
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Imprimimos las cantidades
print(f"La lista numeros tiene {len(numeros)} elementos.")
print(f"La lista pares tiene {len(pares)} elementos.")
print(f"La lista impares tiene {len(impares)} elementos.")

# Ejercicio 4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
unicos = []
for dato in datos:
    if dato not in unicos:
        unicos.append(dato)

print(unicos)

# Ejercicio 5
presentes = ["Ana", "Luis", "Carlos", "Marta", "Sofía", "Jorge", "Lucía", "Diego"]

# Mostramos la lista de presentes
print("Lista de presentes:")
for nombre in presentes:
    print(f"Presente: {nombre}")

#  Preguntamos si quiere eliminar o agregar a alguien
opcion = input("¿Desea agregar un estudiante o eliminar uno? (a/e): ")
if opcion.lower() == 'e':
    nombre_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre_a_eliminar in presentes:
        presentes.remove(nombre_a_eliminar)
        print(f"Estudiante '{nombre_a_eliminar}' eliminado.")
    else:
        print(f"Estudiante '{nombre_a_eliminar}' no encontrado en la lista.")

if opcion.lower() == 'a':
    nombre_a_agregar = input("Ingrese el nombre del estudiante a agregar: ")
    presentes.append(nombre_a_agregar)
    print(f"Estudiante '{nombre_a_agregar}' agregado.")

# Mostramos la lista actualizada
print("Lista actualizada de presentes:")
for nombre in presentes:
    print(f"Presente: {nombre}")


# Ejercicio 6
lista = [1, 2, 3, 4, 5, 6, 7]

# Guardamos el último elemento
ultimo = lista[-1]

# Recorremos la lista de derecha a izquierda
for i in range(len(lista) - 1, 0, -1):
    lista[i] = lista[i - 1]

# Colocamos el último al principio
lista[0] = ultimo

# Ejercicio 7
temperaturas = [
    [12, 22],  # Día 1
    [14, 25],  # Día 2
    [10, 20],  # Día 3
    [13, 27],  # Día 4
    [11, 21],  # Día 5
    [15, 30],  # Día 6
    [9, 19]    # Día 7
]

# Inicializamos
suma_min = 0
suma_max = 0
mayor_amplitud = 0
dia_mayor_amplitud = 0

# Recorremos la matriz
for i in range(len(temperaturas)):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]

    suma_min += minima
    suma_max += maxima

    amplitud = maxima - minima
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1  # Día

# Calculamos promedios
promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

# Mostramos resultados
print(f"Promedio de temperaturas mínimas: {promedio_min:.2f}°C")
print(f"Promedio de temperaturas máximas: {promedio_max:.2f}°C")
print(f"La mayor amplitud térmica fue de {mayor_amplitud}°C y ocurrió el día {dia_mayor_amplitud}.")

# Ejercicio 8
notas = [
    [7, 8, 9],   # Estudiante 1
    [6, 7, 8],   # Estudiante 2
    [9, 9, 10],  # Estudiante 3
    [5, 6, 7],   # Estudiante 4
    [8, 8, 8]    # Estudiante 5
]

# Promedio de cada estudiante (por fila)
print("Promedio por estudiante:")
for i in range(len(notas)):
    promedio_est = sum(notas[i]) / len(notas[i])
    print(f"Estudiante {i+1}: {promedio_est:.2f}")

# Promedio de cada materia (por columna)
print("\nPromedio por materia:")
for j in range(3):  # Hay 3 materias
    suma_materia = 0
    for i in range(5):  # Hay 5 estudiantes
        suma_materia += notas[i][j]
    promedio_mat = suma_materia / 5
    print(f"Materia {j+1}: {promedio_mat:.2f}")