# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Coordenadas de las ciudades
coord = {
    'Aguascalientes': [21.87641043660486, -102.26438663286967],
    'BajaCalifornia': [32.5027, -117.00371],
    'BajaCaliforniaSur': [24.14437, -110.3005],
    'Campeche': [19.8301, -90.53491],
    'Chiapas': [16.75, -93.1167],
    'Chihuahua': [28.6353, -106.0889],
    'CDMX': [19.432713075976878, -99.13318344772986],
    'Coahuila': [25.4260, -101.0053],
    'Colima': [19.2452, -103.725],
    'Durango': [24.0277, -104.6532],
    'Guanajuato': [21.0190, -101.2574],
    'Guerrero': [17.5506, -99.5024],
    'Hidalgo': [20.1011, -98.7624],
    'Jalisco': [20.6767, -103.3475],
    'Mexico': [19.285, -99.5496],
    'Michoacan': [19.701400113725654, -101.20829680213464],
    'Morelos': [18.6813, -99.1013],
    'Nayarit': [21.5085, -104.895],
    'NuevoLeon': [25.6714, -100.309],
    'Oaxaca': [17.0732, -96.7266],
    'Puebla': [19.0414, -98.2063],
    'Queretaro': [20.5972, -100.387],
    'QuintanaRoo': [21.1631, -86.8023],
    'SanLuisPotosi': [22.1565, -100.9855],
    'Sinaloa': [24.8091, -107.394],
    'Sonora': [29.0729, -110.9559],
    'Tabasco': [17.9892, -92.9475],
    'Tamaulipas': [23.731472128815206, -99.15099880731451],
    'Tlaxcala': [19.3181, -98.2375],
    'Veracruz': [19.1738, -96.1342],
    'Yucatan': [20.967, -89.6237],
    'Zacatecas': [22.7709, -102.5833]
}

API_KEY = 'AIzaSyAjtBNMl6V7VEhgA0yAY5qZDuXqBq6yxWI'

@app.route('/', methods=['GET', 'POST'])
def index():
    distance = None
    map_url = None
    if request.method == 'POST':
        start_city = request.form.get('start')
        end_city = request.form.get('end')

        if start_city and end_city:
            start_coords = coord[start_city]
            end_coords = coord[end_city]
            start_str = f"{start_coords[0]},{start_coords[1]}"
            end_str = f"{end_coords[0]},{end_coords[1]}"

            response = requests.get(
                f"https://maps.googleapis.com/maps/api/directions/json?origin={start_str}&destination={end_str}&key={API_KEY}"
            )

            if response.status_code == 200:
                directions = response.json()
                if directions['status'] == 'OK':
                    route = directions['routes'][0]
                    distance = route['legs'][0]['distance']['text']
                    map_url = f"https://www.google.com/maps/embed/v1/directions?key={API_KEY}&origin={start_str}&destination={end_str}&zoom=7"
                else:
                    distance = "No se pudo calcular la ruta"
            else:
                distance = "Error en la solicitud a la API de Google Maps"

    return render_template('index.html', coord=coord, distance=distance, map_url=map_url)

if __name__ == '__main__':
    app.run(debug=True)
