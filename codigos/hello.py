from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from simulated import simulated_annealing, coord, evalua_ruta, rutaS
from Hill_Climb_Iterativa import i_hill_climbing, evalua_rutaH, coordH

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_ruta', methods=['POST'])
def calcular_nueva_ruta():
    if request.form['algoritmo'] == 'simulated_annealing':
        rutaH = simulated_annealing(rutaS, coord)
        distancia_total = evalua_ruta(rutaH, coord)
    elif request.form['algoritmo'] == 'hill_climbing':
        rutaH = i_hill_climbing(coordH)
        distancia_total = evalua_rutaH(rutaH, coordH)
    return jsonify({'ruta': rutaH, 'distancia_total': distancia_total})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)