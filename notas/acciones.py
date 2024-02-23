import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"{usuario[1]}  Vamos a crear una nota")

        titulo = input("Introduce el titulo de la nota: ")
        descripcion = input("Escribe el contenido de la nota: ")

        nota = modelo.Nota(usuario[0],titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"Perfecto has guardado la nota: {nota.titulo}")

        else: 
            print(f"No se pudo guardar la nota ")    