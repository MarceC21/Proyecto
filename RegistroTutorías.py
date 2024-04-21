# Definición de la función para obtener los horarios disponibles para un curso específico
def obtener_horarios_disponibles(curso):
    horarios_por_curso = {
        "1": ["Lunes 8:30 - 9:30", "Miércoles 10:50 - 11:00 ","Jueves 13:40 - 14:40 ", "Viernes 17:00 - 18:00" ],
        "2": ["Martes 12:00-14:00", "Jueves 16:00-18:00"]
    }
    return horarios_por_curso.get(curso, [])

def obtener_tutores_disponibles(curso):
    tutores_disponibles = {
        "1": ["Juan López", "Jaxin Andrade"],   
        "2": ["Lorena Solarzar", "Diego Lorenzana"]
    }
    return tutores_disponibles.get(curso, [])

# Definición de la función para registrar la tutoría
def registrar_tutoria(nombre, carnet, curso, horario, tutor):
    mensaje_confirmacion = f"¡Hola {nombre}! Has sido registrado exitosamente en la tutoría de {curso} con el tutor {tutor} en el horario {horario}."
    return mensaje_confirmacion

# Lista de cursos disponibles
cursos_disponibles = {"1": "Química", "2": "Pensamiento Cuantitativo"}

print("Cursos disponibles:")
for key, value in cursos_disponibles.items():
    print(f"{key}: {value}")

# Ejemplo de uso del programa
curso_elegido = input("Ingrese el número del curso al que desea asignarse: ")

# Obtener y mostrar los horarios disponibles para el curso seleccionado
horarios_disponibles = obtener_horarios_disponibles(curso_elegido)

print("Horarios disponibles:")
for i, horario in enumerate(horarios_disponibles, 1):
    print(f"{i}: {horario}")

horario_elegido = int(input("Seleccione el número del horario al que desea inscribirse: "))
horario_elegido = horarios_disponibles[horario_elegido - 1]

# Obtener y mostrar los tutores disponibles para el curso y horario seleccionados
tutores_disponibles = obtener_tutores_disponibles(curso_elegido)

print("Tutores disponibles:")
for i, tutor in enumerate(tutores_disponibles, 1):
    print(f"{i}: {tutor}")

tutor_elegido = int(input("Seleccione el número del tutor al que desea inscribirse: "))
tutor_elegido = tutores_disponibles[tutor_elegido - 1]

# Solicitar la información personal al usuario
nombre_usuario = input("Ingrese su nombre completo: ")
carnet_usuario = input("Ingrese su número de carnet: ")

# Llamar a la función para registrar la tutoría
mensaje_confirmacion = registrar_tutoria(nombre_usuario, carnet_usuario, cursos_disponibles[curso_elegido], horario_elegido, tutor_elegido)

# Mostrar el mensaje de confirmación
print(mensaje_confirmacion)