# Diccionario de productos y su stock
stock_productos = {
    "lapiz": 10,
    "cuaderno": 5,
    "goma": 3
}

# Mostrar menú de opciones
print("Gestión de stock de productos")
producto = input("Ingresá el nombre del producto a consultar o modificar: ").strip().lower()

if producto in stock_productos:
    print(f"El stock actual de '{producto}' es: {stock_productos[producto]} unidades.")
    agregar = input("¿Querés agregar unidades? (s/n): ").strip().lower()
    if agregar == "s":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += unidades
        print(f"Stock actualizado: {stock_productos[producto]} unidades.")
else:
    print(f"El producto '{producto}' no existe en el sistema.")
    crear = input("¿Querés agregarlo como nuevo producto? (s/n): ").strip().lower()
    if crear == "s":
        unidades = int(input("¿Cuántas unidades tiene?: "))
        stock_productos[producto] = unidades
        print(f"Producto '{producto}' agregado con {unidades} unidades.")

# Mostrar estado final del stock
print("\nEstado actual del stock:")
for nombre, cantidad in stock_productos.items():
    print(f"{nombre}: {cantidad} unidades")
