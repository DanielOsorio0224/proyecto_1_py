import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("\nOk vamos a registrarte en el sistema")

        nombre = input("Cual es tu nombre: ")
        apellidos = input("apellidos: ")
        email = input("Ingresa tu correo: ")
        password = input("Ingresa tu contraseña: ")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te registraste bien")
    def login(self):
        print("\nIdentificate en el sistema")

        email = input("Ingresa tu correo: ")
        password = input("Ingresa tu contraseña") 