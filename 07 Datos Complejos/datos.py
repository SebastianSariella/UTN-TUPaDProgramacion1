# Ejercicio 1
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# Ejercicio 3
lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

# Ejercicio 4
contactos = {}

# Cargar 5 contactos
print("📱 Carga de contactos telefónicos")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto #{i+1}: ").strip()
    numero = input(f"Ingresá el número de {nombre}: ").strip()
    contactos[nombre] = numero

# Consultar un contacto
print("\nConsulta de número telefónico")
consulta = input("Ingresá el nombre que querés buscar: ").strip()

if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print(f"No se encontró el contacto '{consulta}'.")

# Ejercicio 5
frase = input("Ingresá una frase: ").strip().lower()

palabras = frase.split()

palabras_unicas = set(palabras)
print("\nPalabras únicas:")
print(palabras_unicas)

conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print("\nCantidad de veces que aparece cada palabra:")
for palabra, cantidad in conteo.items():
    print(f"{palabra}: {cantidad}")

# Ejercicio 6
alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno #{i+1}: ").strip()
    print(f"Ingresá las 3 notas de {nombre}:")
    nota1 = float(input("  Nota 1: "))
    nota2 = float(input("  Nota 2: "))
    nota3 = float(input("  Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

# Mostrar promedio de cada alumno
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# Ejercicio 7
parcial1 = {101, 102, 103, 104, 105}
parcial2 = {104, 105, 106, 107}

ambos = parcial1 & parcial2
print("Aprobó ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobó solo uno de los dos:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobó al menos un parcial:", al_menos_uno)


