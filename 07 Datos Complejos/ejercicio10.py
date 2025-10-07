# Diccionario original: país → capital
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

# Crear diccionario vacío para invertir
capitales = {}

# Recorrer el diccionario original y construir el nuevo
for pais, capital in paises.items():
    capitales[capital] = pais

# Mostrar el diccionario invertido
print(capitales)