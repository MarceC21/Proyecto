import user_management
import tutoring_management
opcion="algo"
while opcion!="3": 
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        user_management.registrarse()
    elif opcion == "2":
        usuario = user_management.iniciar_sesion()
        if usuario:
            mensaje_bienvenida = "¡Bienvenido, {}!".format(usuario["correo"])
            print(mensaje_bienvenida)
            menu="algo"
            while menu!="4":
                print("\nMenú de Tutorías:")
                print("1. Ver clases disponibles para tutorías")
                print("2. Ver tutorías asignadas")
                print("3. Dejar un comentario")
                print("4. Cerrar sesión")
                
                menu = input("Seleccione una opción: ")
                
                if menu == "1":
                    tutoring_management.ver_clases_disponibles()
                elif menu == "2":
                    tutoring_management.ver_tutorias_asignadas(usuario)
                elif menu == "3":
                    tutoring_management.dejar_comentario(usuario)
                elif menu == "4":
                    print("Cerrando sesión...")
                    break
                else:
                    print("Opción inválida. Por favor, inténtelo de nuevo.")

    elif opcion == "3":
        print("¡Hasta luego!")
    else:
        print("Opción inválida. Por favor, inténtelo de nuevo.")

