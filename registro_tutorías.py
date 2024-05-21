import pandas as pd
import os

# Leer el archivo CSV de tutores
tutorias = pd.read_csv("clases.csv")

# Definición de la función para obtener los horarios disponibles para un curso específico
def horarios(curso):
    horarios = tutorias[tutorias['clases'] == curso]['horario'].unique()
    return list(horarios)

def tutores(curso, horario):
    tutores = tutorias[(tutorias['clases'] == curso) & (tutorias['horario'] == horario)]
    return tutores[['tutor', 'correo', 'telefono', 'aniocarrera', 'carrera', 'informacionadicional']]

def registro(nombre, carnet, curso, horario, tutor):
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
cursos = tutorias['clases'].unique()
cursos_lista = {str(i+1): curso for i, curso in enumerate(cursos)}

print("Cursos disponibles:")
for key, value in cursos_lista.items():
    print(f"{key}: {value}")

# Solicitar y validar el curso elegido
curso_elegir = input("Ingrese el número del curso al que desea asignarse: ")
while curso_elegir not in cursos_lista:
    print("Curso no válido. Intente de nuevo.")
    curso_elegido_key = input("Ingrese el número del curso al que desea asignarse: ")

curso_elegido = cursos_lista[curso_elegir]

# Obtener y mostrar los horarios disponibles para el curso seleccionado
horarios = horarios(curso_elegido)
print("Horarios disponibles:")
for i, horario in enumerate(horarios, 1):
    print(f"{i}: {horario}")

horario_selec = int(input("Seleccione el número del horario al que desea inscribirse: "))
horario_elegido = horarios[horario_selec - 1]

# Obtener y mostrar los tutores disponibles para el curso y horario seleccionados
tutores = tutores(curso_elegido, horario_elegido)
print("Tutores disponibles:")
for i, row in enumerate(tutores.itertuples(), 1):
    print(f"{i}: {row.tutor} (Correo: {row.correo}, Teléfono: {row.telefono}, Año de carrera: {row.aniocarrera}, Carrera: {row.carrera}, Información adicional: {row.informacionadicional})")

tutor_selec = int(input("Seleccione el número del tutor al que desea inscribirse: "))
tutor_elegido = tutores.iloc[tutor_selec- 1]['tutor']

# Solicitar la información del usuario
nombre_usuario = input("Ingrese su nombre completo: ")
carnet_usuario = input("Ingrese su número de carnet: ")

# Registrar la tutoría en el archivo CSV correspondiente
registro(nombre_usuario, carnet_usuario, curso_elegido, horario_elegido, tutor_elegido)
