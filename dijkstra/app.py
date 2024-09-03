from flask import Flask, render_template, request
from dijkstra import dijkstra, grafo

# Crear la aplicación Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None

    if request.method == 'POST':
        inicio = request.form.get('inicio')
        fin = request.form.get('fin')

        if inicio and fin:
            camino, costo = dijkstra(grafo, inicio, fin)
            resultado = {'camino': camino, 'costo': costo}

    return render_template('index.html', resultado=resultado)

# Ejecutar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
