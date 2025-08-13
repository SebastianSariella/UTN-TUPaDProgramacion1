# Ejercicio 1
print("Hola Mundo!")

# Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su ciudad de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4
radio = float(input("Ingrese el radio de un círculo: "))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio
print(f"El área del círculo es: {area} y el perímetro es {perimetro}.")

# Ejercicio 5
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

# Ejercicio 6
numero = int(input("Ingrese un número: "))
print(f"{numero}x1 = {numero * 1}")
print(f"{numero}x2 = {numero * 2}")
print(f"{numero}x3 = {numero * 3}")
print(f"{numero}x4 = {numero * 4}")
print(f"{numero}x5 = {numero * 5}")
print(f"{numero}x6 = {numero * 6}")
print(f"{numero}x7 = {numero * 7}")
print(f"{numero}x8 = {numero * 8}")
print(f"{numero}x9 = {numero * 9}")
print(f"{numero}x10 = {numero * 10}")

# Ejercicio 7 
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} / {num2} = {division}")

# Ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc}")

# Ejercicio 9
grados_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
grados_fahrenheit = (grados_celsius * 9/5) + 32
print(f"{grados_celsius} grados Celsius equivalen a {grados_fahrenheit} grados Fahrenheit.")

# Ejercicio 10
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio}")