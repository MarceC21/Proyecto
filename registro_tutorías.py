import pandas as pd
import os

# Definición de la función para obtener los horarios disponibles para un curso específico
def obtener_horarios_disponibles(curso):
    horarios_por_curso = {
        "1": ["Lunes 8:30 - 9:30", "Miércoles 10:50 - 11:00 ","Jueves 13:40 - 14:40 ", "Viernes 17:00 - 18:00" ],
        "2": ["Martes 8:30 - 9:30", "Miércoles 10:50 - 11:50", "Jueves 13:40 - 14:40", "Viernes 18:00 - 19:00"  ],
        "3": ["Lunes 8:30 - 9:30", "Martes 10:50 - 11:50", "Jueves 13:40 - 14:40", "Viernes 18:00 - 19:00"  ],
        "4": ["Martes 10:00 - 11:00", "Miércoles 12:00 - 13:00", "Viernes 15:00 - 16:00", "Viernes 17:50 - 18:50"  ],
        "5": ["Lunes 13:00 - 14:00", "Martes 09:00 - 10:00", "Miércoles 11:00 - 12:00", "Viernes 14:00 - 15:00"  ],
        "6": ["Martes 8:00 - 10:00", "Miércoles 11:00 - 12:00", "Jueves 12:00 - 13:00", "Viernes 15:30 - 17:30"  ],
    }
    return horarios_por_curso.get(curso, [])

def obtener_tutores_disponibles(curso):
    tutores_disponibles = {
        "1": ["Juan López", "Jaxin Andrade"],   
        "2": ["Lorena Solarzar", "Diego Lorenzana"],
        "3": ["Dionisio Pérez", "Luisa Hernandez"],
        "4": ["Santiago López", "Javier Sánchez"],
        "5": ["Sebastían Rodas", "José Pérez"],
        "6": ["Santiago Sánchez", "Andrés Salazar"]
    }
    return tutores_disponibles.get(curso, [])

def registrar_tutoria(nombre, carnet, curso, horario, tutor):
    # Nombre del archivo CSV basado en curso, tutor y horario
    filename = f"{curso}_{tutor}_{horario.replace(':', '').replace(' ', '_')}.csv"

    # Crear DataFrame con la información del registro
    df = pd.DataFrame([{"Curso": curso, "Tutor": tutor, "Horario": horario, "Nombre": nombre, "Carnet": carnet}])

    # Si el archivo existe, append al archivo existente
    if os.path.isfile(filename):
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, mode='w', header=True, index=False)
    
    print(f"Registro guardado en {filename}")

# Lista de cursos disponibles
cursos_disponibles = {"1": "Química", "2": "Pensamiento Cuantitativo", "3": "Ciencias de la vida", "4": "Física", "5": "Cálculo 1", "6": "Comunicación efectiva" }

print("Cursos disponibles:")
for key, value in cursos_disponibles.items():
    print(f"{key}: {value}")

# Solicitar y validar el curso elegido
curso_elegido = input("Ingrese el número del curso al que desea asignarse: ")
while curso_elegido not in cursos_disponibles:
    print("Curso no válido. Intente de nuevo.")
    curso_elegido = input("Ingrese el número del curso al que desea asignarse: ")

# Obtener y mostrar los horarios disponibles para el curso seleccionado
horarios_disponibles = obtener_horarios_disponibles(curso_elegido)
print("Horarios disponibles:")
for i, horario in enumerate(horarios_disponibles, 1):
    print(f"{i}: {horario}")

horario_elegido = int(input("Seleccione el número del horario al que desea inscribirse: "))
horario_elegido = horarios_disponibles[horario_elegido - 1]

# Obtener y mostrar los tutores disponibles para el curso seleccionado
tutores_disponibles = obtener_tutores_disponibles(curso_elegido)
print("Tutores disponibles:")
for i, tutor in enumerate(tutores_disponibles, 1):
    print(f"{i}: {tutor}")

tutor_elegido = int(input("Seleccione el número del tutor al que desea inscribirse: "))
tutor_elegido = tutores_disponibles[tutor_elegido - 1]

# Solicitar la información del usuario
nombre_usuario = input("Ingrese su nombre completo: ")
carnet_usuario = input("Ingrese su número de carnet: ")

# Registrar la tutoría en el archivo CSV correspondiente
registrar_tutoria(nombre_usuario, carnet_usuario, cursos_disponibles[curso_elegido], horario_elegido, tutor_elegido)
