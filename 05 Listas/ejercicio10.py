matriz = [
    [10, 12, 14, 16, 8, 4, 15], # Producto 1
    [1, 4, 8, 3, 8, 5, 6], # producto 2
    [20, 24, 18, 31, 28, 15, 17], # producto 3
    [1, 1, 3, 2, 1, 5, 7] # producto 4
]

# Total vendido por cada producto
sumatoria = [0, 0, 0, 0]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        sumatoria[i] += matriz[i][j]

for i in range(len(sumatoria)):
    print(f"Total vendido del producto {i+1}: {sumatoria[i]}")

# Sumatoria por día
sumatoria_dia = [0, 0, 0, 0, 0, 0, 0]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        sumatoria_dia[j] += matriz[i][j]

dia_mas_vendido = sumatoria_dia[0]
indice_dia_mas_vendido = 0
for j in range(len(sumatoria_dia)):
    if sumatoria_dia[j] > dia_mas_vendido:
        dia_mas_vendido = sumatoria_dia[j]
        indice_dia_mas_vendido = j

print(f"El día que más se vendió fue el día {indice_dia_mas_vendido + 1} con {dia_mas_vendido} unidades vendidas.")
    
# Producto más vendido
producto_mas_vendido = sumatoria[0]
indice_producto_mas_vendido = 0
for i in range(len(sumatoria)):
    if sumatoria[i] > producto_mas_vendido:
        producto_mas_vendido = sumatoria[i]
        indice_producto_mas_vendido = i

print(f"El producto más vendido fue el producto {indice_producto_mas_vendido + 1} con {producto_mas_vendido} unidades vendidas.")








