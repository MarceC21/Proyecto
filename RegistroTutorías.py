import pandas as pd
import os

# Leer el archivo CSV de tutores
df_tutores = pd.read_csv("clases.csv")

# Definición de la función para obtener los horarios disponibles para un curso específico
def obtener_horarios_disponibles(curso):
    horarios = df_tutores[df_tutores['clases'] == curso]['horario'].unique()
    return list(horarios)

def obtener_tutores_disponibles(curso, horario):
    tutores = df_tutores[(df_tutores['clases'] == curso) & (df_tutores['horario'] == horario)]
    return tutores[['tutor', 'correo', 'telefono', 'aniocarrera', 'carrera', 'informacionadicional']]

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
cursos_disponibles = df_tutores['clases'].unique()
cursos_disponibles_dict = {str(i+1): curso for i, curso in enumerate(cursos_disponibles)}

print("Cursos disponibles:")
for key, value in cursos_disponibles_dict.items():
    print(f"{key}: {value}")

# Solicitar y validar el curso elegido
curso_elegido_key = input("Ingrese el número del curso al que desea asignarse: ")
while curso_elegido_key not in cursos_disponibles_dict:
    print("Curso no válido. Intente de nuevo.")
    curso_elegido_key = input("Ingrese el número del curso al que desea asignarse: ")

curso_elegido = cursos_disponibles_dict[curso_elegido_key]

# Obtener y mostrar los horarios disponibles para el curso seleccionado
horarios_disponibles = obtener_horarios_disponibles(curso_elegido)
print("Horarios disponibles:")
for i, horario in enumerate(horarios_disponibles, 1):
    print(f"{i}: {horario}")

horario_elegido_index = int(input("Seleccione el número del horario al que desea inscribirse: "))
horario_elegido = horarios_disponibles[horario_elegido_index - 1]

# Obtener y mostrar los tutores disponibles para el curso y horario seleccionados
tutores_disponibles_df = obtener_tutores_disponibles(curso_elegido, horario_elegido)
print("Tutores disponibles:")
for i, row in enumerate(tutores_disponibles_df.itertuples(), 1):
    print(f"{i}: {row.tutor} (Correo: {row.correo}, Teléfono: {row.telefono}, Año de carrera: {row.aniocarrera}, Carrera: {row.carrera}, Información adicional: {row.informacionadicional})")

tutor_elegido_index = int(input("Seleccione el número del tutor al que desea inscribirse: "))
tutor_elegido = tutores_disponibles_df.iloc[tutor_elegido_index - 1]['tutor']

# Solicitar la información del usuario
nombre_usuario = input("Ingrese su nombre completo: ")
carnet_usuario = input("Ingrese su número de carnet: ")

# Registrar la tutoría en el archivo CSV correspondiente
registrar_tutoria(nombre_usuario, carnet_usuario, curso_elegido, horario_elegido, tutor_elegido)
