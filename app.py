from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import csv
import os
from funciones import * 

app = Flask(__name__)

# Ruta para el formulario de inicio de sesión
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('uname')
        password = request.form.get('psw')
        email = request.form.get('email')
        
        # Verificar las credenciales del usuario
        if verificacion(usuario, password, email):
            print("Credenciales correctas. Redirigiendo a la página de tutorías...")
            return redirect(url_for('tutorias'))
        else:
            return render_template('login.html', mensaje='Credenciales incorrectas. Por favor, inténtalo de nuevo.')
    return render_template('login.html')  # Renderiza la página de inicio de sesión para los métodos GET

# Función para verificar las credenciales del usuario
def verificacion(usuario, password, email):
    with open('usuarios.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Usuario'] == usuario and row['Clave'] == password and row['Correo'] == email:
                return True
    return False

# Ruta para la página de tutorías
@app.route('/tutorias')
def tutorias():
    return render_template('tutorias.html')  # Aquí renderiza la página de tutorías que desees

# Función de registro a una tutoría
def registro(nombre, carnet, curso, horario, tutor):
    # Nombre del archivo CSV basado en curso, tutor y horario
    filename = f"{curso}_{tutor}_{horario.replace(':', '').replace(' ', '_')}.csv"
    
    # Crear DataFrame con la información del registro
    tutorias = pd.DataFrame([{"Curso": curso, "Tutor": tutor, "Horario": horario, "Nombre": nombre, "Carnet": carnet}])

    # Si el archivo existe, append al archivo existente
    if os.path.isfile(filename):
        tutorias.to_csv(filename, mode='a', header=False, index=False)
    else:
        tutorias.to_csv(filename, mode='w', header=True, index=False)
    
    print(f"Registro guardado en {filename}")

# Ruta para recibir datos del formulario y registrar la tutoría
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form.get('nombre')
        carnet = request.form.get('carnet')
        tutor = request.form.get('tutor')
        horario = request.form.get('horario')
        curso = request.form.get('curso')
        
        # Guardar los datos en un archivo CSV
        registro(nombre, carnet, curso, horario, tutor)
        
        return redirect(url_for('gracias'))

# Ruta para mostrar el mensaje de agradecimiento
@app.route('/gracias')
def gracias():
    return "Gracias por enviar la información. Te contactarán en breves para coordinar todo."

if __name__ == '__main__':
    app.run(debug=True)
