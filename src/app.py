from flask import Flask, render_template, request, jsonify
import os
from dao.estudiante_dao import EstudianteDAO
from dto.estudiante_dto import EstudianteDTO
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder=template_dir)
estudiante_dao = EstudianteDAO()
# Ruta principal para mostrar el formulario
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para manejar el envío de datos del formulario
@app.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    # Obtener datos del formulario
    cedula = request.form.get('document')
    nombres = request.form.get('name')
    apellidos = request.form.get('surname')
    direccion_residencia = request.form.get('address')
    lat_res = float(request.form.get('latitude'))
    lon_res = float(request.form.get('longitude'))
    direccion_trabajo = request.form.get('work_address')
    lat_trab = float(request.form.get('work_latitude'))
    lon_trab = float(request.form.get('work_longitude'))

    estudiante = EstudianteDTO(cedula, nombres, apellidos, direccion_residencia, lat_res, lon_res, direccion_trabajo, lat_trab, lon_trab)
    estudiante_dao.add_estudiante(estudiante)

    return jsonify({"message": "Estudiante registrado exitosamente"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)