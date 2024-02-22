from usuarios import acciones

print("""
Acciones Disponibles:
      -registro
      -login
""")
hacer = acciones.Acciones()
accion = input("Que quieres hacer?? ")

if accion == "registro":
    hacer.registro()
elif accion == "login":
    hacer.login()