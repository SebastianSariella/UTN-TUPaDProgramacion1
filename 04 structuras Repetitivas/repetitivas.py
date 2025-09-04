import random

# Ejercicio 1
for i in range(0, 101):
    print(i)

# Ejercicio 2
num = int(input("Ingrese un número: "))
num = abs(num)
cant_digitos = 0
if num == 0:
    cant_digitos = 1
else:
    while num > 0:
        num //= 10
        cant_digitos += 1
print("Cantidad de dígitos:", cant_digitos)

# Ejercicio 3
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
inicio = min(num1, num2)
fin = max(num1, num2)
sumatoria = 0
for i in range(inicio+1, fin):
    sumatoria += i
print("Sumatoria:", sumatoria)

# Ejercicio 4
num = int(input("Ingrese un número entero (Ingrese 0 para detener): "))
sumatoria = 0
while num != 0:
    sumatoria += num
    num = int(input("Ingrese otro número entero (Ingrese 0 para detener): "))
print("Sumatoria total:", sumatoria)

# Ejercicio 5
num = random.randint(1, 10)
num_user = int(input("Adivina el número (entre 1 y 10): "))
intentos = 1
while num_user != num:
    num_user = int(input("Incorrecto. Intenta de nuevo: "))
    intentos += 1
print("¡Correcto! Número de intentos:", intentos)

# Ejercicio 6
# Imprimir numeros pares del 0 al 100 en orden descendente (Sin incluir estos mismos)
for i in range(98, 0, -2):
    print(i)

# Ejercicio 7
num_inicial = 0
sumatoria = 0
num_final = int(input("Ingrese un número entero positivo: "))
while num_final <= 0:
    num_final = int(input("Número inválido. Ingrese un número entero positivo: "))
# Si se desea excluir el num_final, usar range(num_inicial, num_final)
for i in range(num_inicial, num_final+1):
    sumatoria += i
print("Sumatoria:", sumatoria)

# Ejercicio 8
par = 0
impar = 0
positivos = 0
negativos = 0
for i in range(100):
    num = int(input("Ingrese un número entero:"))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("Cantidad de números pares:", par)
print("Cantidad de números impares:", impar)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

# Ejercicio 9
sumatoria = 0
for i in range(100):
    num = int(input("Ingrese un número entero:"))
    sumatoria += num
promedio = sumatoria / 100
print("Promedio:", promedio)

# Ejercicio 10
num = int(input("Ingrese un número: "))
invertido = 0

while num > 0:
    digito = num % 10        # tomo el último dígito
    invertido = invertido * 10 + digito
    num //= 10               # elimino el último dígito

print("Número invertido:", invertido)