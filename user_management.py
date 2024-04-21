
ARCHIVO_USUARIOS = "datos_usuarios.txt"

def registrarse():
    correo = input("Ingrese su correo electrónico: ")
    if not correo.endswith("@uvg.edu.gt"):
        print("Dominio de correo electrónico no válido. Por favor, utilice una dirección de correo electrónico válida de la UVG.")
        return
    contraseña1 = input("Ingrese su contraseña: ")
    contraseña2 = input("Confirme su contraseña: ")
    if contraseña1 != contraseña2:
        print("Las contraseñas no coinciden. Por favor, inténtelo de nuevo.")
        return

    with open(ARCHIVO_USUARIOS, "a") as archivo:
        archivo.write("{} {}\n".format(correo, contraseña1))
    print("Registro exitoso. Ahora puede iniciar sesión.")

def iniciar_sesion():
    correo = input("Ingrese su correo electrónico: ")
    contraseña = input("Ingrese su contraseña: ")

    with open(ARCHIVO_USUARIOS, "r") as archivo:
        for linea in archivo:
            correo_guardado, contraseña_guardada = linea.strip().split()
            if correo == correo_guardado and contraseña == contraseña_guardada:
                return {"correo": correo}
    print("Correo electrónico o contraseña incorrectos. Por favor, inténtelo de nuevo.")
    return None
