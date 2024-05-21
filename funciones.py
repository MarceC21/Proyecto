import csv

usuario = ""


def registro():
    global usuario
    with open("logiin.csv", mode="a", newline="") as f:
        es = csv.writer(f, delimiter=",")
        correo = input("Por favor, escriba su correo de la Universidad: ")
        if correo.endswith("@uvg.edu.gt"):
            contra = input("Por favor, escriba su contraseña: ")
            contra2 = input("Por favor, repita su contraseña: ")
            if contra == contra2:
                es.writerow([correo, contra])
                usuario = correo
                print("¡Su registro ha sido exitoso!")
            else:
                print("Vuelva a intentarlo, algo salió mal.")
        else:
            print("Ingreso su correo de manera incorrecta!")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def inicio():
    global usuario
    correo = input("Por favor escriba su correo de la Universidad: ")
    if correo.endswith("@uvg.edu.gt"):
        contra = input("Por favor escriba su contraseña: ")
        with open("logiin.csv", mode="r", newline="") as f:
            leer = csv.reader(f, delimiter=",")
            for i in leer:
                if i[0] == correo and i[1] == contra:
                    usuario = correo
                    print("Inicio sesión correctamente!")
                    menuprincipal()
                    return True
        print("Por favor intente nuevamente algo salió mal.")
        return False
    else:
        print("Ingreso su correo de manera incorrecta!")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def menuprincipal():
    global usuario
    opcionmenup = ""
    while opcionmenup != '4':
        print("\nBIENVENIDO A TUTORIAS UVG", usuario)
        print("1. Explorar Clases Disponibles para Tutorías.")
        print("2. Informacion General.")
        print("3. Dejar Comentarios.")
        print("4. Cerrar Sesion")
        opcionmenup = input(" Eleccion: ")
        if opcionmenup == '4':
            print("Hasta pronto!")
        elif opcionmenup == '1':
            print("Clases Disponibles.")
            explorar_clases()
        elif opcionmenup == '2':
            print("\nHecho por y para estudiantes de la UVG, este programa está diseñado con cariño y dedicación para facilitar tu proceso de encontrar y gestionar tutorías. Nuestro objetivo es brindarte una herramienta intuitiva y eficiente que te permita explorar las clases disponibles, conocer a nuestros tutores especializados y acceder a la ayuda que necesitas para sobresalir en tus estudios. Aquí encontrarás todo lo necesario para organizar tus sesiones de tutoría, mejorar tu rendimiento académico y sentirte acompañado en tu camino universitario. ¡Gracias por ser parte de esta comunidad de aprendizaje y apoyo mutuo!")
            print("\nVisión: \nSer la plataforma líder en la facilitación de tutorías universitarias, ofreciendo a los estudiantes de la UVG una herramienta intuitiva y eficiente para encontrar y gestionar sesiones de tutoría. Nuestra visión es convertirnos en el punto de referencia para los estudiantes que buscan apoyo académico, proporcionando acceso fácil a una amplia gama de clases y tutores altamente calificados. Buscamos crear una comunidad de aprendizaje y apoyo mutuo donde los estudiantes puedan sobresalir en sus estudios y alcanzar su máximo potencial académico.")
            print("\nMisión: \nNuestra misión es proporcionar una plataforma accesible y fácil de usar que conecte a los estudiantes de la UVG con tutores especializados en diversas áreas académicas. Nos comprometemos a ofrecer un servicio de alta calidad que satisfaga las necesidades individuales de cada estudiante, brindando soporte personalizado y recursos educativos que fomenten el éxito académico. Además, nos esforzamos por promover un entorno de colaboración y aprendizaje mutuo, donde los estudiantes puedan compartir sus conocimientos y experiencias para beneficio de toda la comunidad universitaria.")
        elif opcionmenup == '3':
            comentariosusuarios()
        else:
            print("Esa opcion no esta disponible!")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def comentariosusuarios():
    global usuario
    comentario = input("Por favor, escribe tu comentario sobre el programa: ")
    with open("comnt.csv", mode="a", newline="") as archivo:
        escritor_csv = csv.writer(archivo, delimiter=",")
        escritor_csv.writerow([usuario, comentario])
    print("¡Gracias por tu comentario!")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def explorar_clases():
    clasesdisponibles = {}
    with open("clases.csv", mode="r", newline="", encoding="utf-8") as archivo:
        leearchivoclases = csv.reader(archivo, delimiter=",")
        for fila in leearchivoclases:
            clase = fila[0]
            if clase not in clasesdisponibles:
                clasesdisponibles[clase] = []
            clasesdisponibles[clase].append(fila)

    enumerarclases = list(clasesdisponibles.keys())
    enumerarclases.sort()

    print("\nClases Disponibles para Tutorías:")
    for x, clase in enumerate(enumerarclases, 1):
        print(f"{x}. {clase}")

    seleccion = int(input("Seleccione una clase por su número: "))
    selecciondelusuario = enumerarclases[seleccion - 1]

    print(f"\nInformación de tutores para {selecciondelusuario}:")
    i = 1
    for tutor in clasesdisponibles[selecciondelusuario]:
        print(f"{i}. Tutor: {tutor[1]}")
        print(f"    Correo: {tutor[2]}")
        print(f"    Teléfono: {tutor[3]}")
        print(f"    Año de carrera: {tutor[4]}")
        print(f"    Carrera: {tutor[5]}")
        print(f"    Información adicional: {tutor[6]}")
        print()
        i += 1
