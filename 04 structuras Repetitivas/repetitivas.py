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