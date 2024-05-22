from flask import Flask, request, render_template, redirect, url_for, session
import pandas as pd
import os
import csv
from funciones import * 
app = Flask(__name__)


#Funcion de registro a una tutoria
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


# Ruta para mostrar el formulario
@app.route('/')
def index():
    return render_template('PaginaWeb.html')


# Donde obtiene los datos del html
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form.get('nombre')
        carnet = request.form.get('carnet')
        tutor = request.form.get('tutor')
        horario = request.form.get('horario')

        curso=request.form.get('mainInfo')
        # Guardar los datos en un archivo CSV
        registro(nombre, carnet, curso, horario, tutor)
        
        
        return redirect(url_for('gracias'))

# Ruta para mostrar el mensaje de agradecimiento
@app.route('/gracias')
def gracias():
    return "Gracias por enviar la información. Te contactarán en breves para coordinar todo."

app.run(debug=True)
