import usuarios.usuario as modelo
import notas.acciones
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

        try:
            email = input("Ingresa tu correo: ")
            password = input("Ingresa tu contraseña: ") 

            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\n Bienvenido {login[1]}, te has registrado el {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Login incorrecto")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)                              
        """)        

        accion = input("Que quieres hacer: ")
        hacer = notas.acciones.Acciones()

        if accion == "crear":            
            hacer.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            print("Mira tus notas")    

        elif accion == "eliminar":
            print("Que nota vas a eliminar")    

        elif accion == "salir":
            print(f"Hasta pronto {usuario[1]}")
            exit()                