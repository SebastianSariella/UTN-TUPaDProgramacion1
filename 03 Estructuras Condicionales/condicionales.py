from statistics import mode, median, mean
import random

# Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Eres mayor de edad.")

# Ejercicio 2
nota = int(input("Ingrese su calificación (0-10): "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3
numero_par = int(input("Ingrese un número par: "))
if numero_par % 2 == 0:
    print("El número es par.")
else:
    print("Por favor, ingrese un número par.")

# Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño.")
elif edad >= 12 and edad < 18:
    print("Adolescente.")
elif edad >= 18 and edad < 30:
    print("Adulto joven.")
else:
    print("Adulto.")

# Ejercicio 5
password = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta.")
    
# Ejercicio 6
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha.")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda.")
elif media == mediana and mediana == moda:
    print("No hay sesgo.")
else:
    print("?")

# Ejercicio 7
frase = input("Ingrese una frase/palabra: ")
if frase[-1].lower() in "aeiou":
    print(frase + "!")
else:
    print(frase)

# Ejercicio 8
nombre = input("Ingrese su nombre: ")

print("1. Si quiere su nombre en mayúsculas. ")
print("2. Si quiere su nombre en minúsculas. ")
print("3. Si quiere su nombre con la primera letra en mayúscula. ")

opcion = int(input("Ingrese una opción (1, 2 o 3): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

# Ejercicio 9
magnitud = float(input("Ingrese la magnitud del sismo: "))
if magnitud < 3:
    print("Muy leve.")
elif magnitud >= 3 and magnitud < 4:
    print("Leve.")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado.")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte.")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte.")
elif magnitud >= 7:
    print("Extremo.")

# Ejercicio 10
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿En qué mes estamos? (1-12): "))
dia = int(input("¿Qué día del mes es?: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print("La estación es:", estacion)



