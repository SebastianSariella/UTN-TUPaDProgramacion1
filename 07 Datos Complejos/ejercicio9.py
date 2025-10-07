# Agenda con eventos
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "18:30"): "Gimnasio",
    ("jueves", "09:00"): "Consulta médica"
}

# Consulta de evento
print("Consulta de agenda")
dia = input("Ingresá el día (ej. lunes): ").strip().lower()
hora = input("Ingresá la hora (ej. 10:00): ").strip()

clave = (dia, hora)

if clave in agenda:
    print(f"El {dia} a las {hora} tenés: {agenda[clave]}")
else:
    print(f"No hay eventos registrados para {dia} a las {hora}.")
