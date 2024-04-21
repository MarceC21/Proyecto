
ARCHIVO_CLASES = "datos_clases.txt"
ARCHIVO_TUTORIAS_ASIGNADAS = "tutorias_asignadas.txt"
ARCHIVO_COMENTARIOS = "comentarios.txt"

def ver_clases_disponibles():
    with open(ARCHIVO_CLASES, "r") as archivo:
        clases = archivo.readlines()
    print("\nClases disponibles para tutorías: ")
    for indice, nombre_clase in enumerate(clases, start=1):
        print("{}. {}".format(indice, nombre_clase.strip()))

def ver_tutorias_asignadas(usuario):
    correo = usuario["correo"]
    tutorias_asignadas = []
    with open(ARCHIVO_TUTORIAS_ASIGNADAS, "r") as archivo:
        for linea in archivo:
            correo_usuario, nombre_clase, tutor = linea.strip().split(",")
            if correo_usuario == correo:
                tutorias_asignadas.append((nombre_clase, tutor))
    if tutorias_asignadas:
        print("Sus tutorías asignadas:")
        for nombre_clase, tutor in tutorias_asignadas:
            print("- Clase: {}, Tutor: {}".format(nombre_clase, tutor))
    else:
        print("Aún no se le han asignado tutorías.")

def dejar_comentario(usuario):
    correo = usuario["correo"]
    comentario = input("Ingrese su comentario: ")
    with open(ARCHIVO_COMENTARIOS, "a") as archivo:
        archivo.write("{}: {}\n".format(correo, comentario))
    print("Comentario enviado exitosamente.")
