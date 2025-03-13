from flask import Flask, jsonify, request
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

# Base de datos simulada
patients = []

# Endpoint para registrar pacientes
@app.route('/patients/create', methods=['POST'])
def register_patient():
    data = request.get_json()
    patient = {
        'id': len(patients) + 1,
        'name': data['name'],
        'age': data['age'],
        'medication': data['medication'],
        'glucose_history': data['glucose_history']
    }
    patients.append(patient)
    return jsonify(patient), 201

# Endpoint para obtener la lista de pacientes
@app.route('/patients', methods=['GET'])
def get_patients():
    return jsonify(patients), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
