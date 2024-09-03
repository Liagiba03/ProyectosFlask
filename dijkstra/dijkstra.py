import heapq

# Algoritmo de Dijkstra para encontrar el camino más corto
def dijkstra(grafo, inicio, fin):
    # Cola de prioridad para seleccionar el nodo con la distancia más baja
    cola_prioridad = [(0, inicio)]
    # Diccionario para almacenar la distancia mínima a cada nodo
    distancias = {nodo: float('inf') for nodo in grafo}
    # Inicializar la distancia al nodo de inicio
    distancias[inicio] = 0
    # Diccionario para rastrear predecesores (para reconstruir el camino)
    predecesores = {}

    # Mientras haya nodos en la cola de prioridad
    while cola_prioridad:
        # Obtener el nodo con la distancia más baja
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        # Si hemos llegado al nodo de destino, podemos salir del bucle
        if nodo_actual == fin:
            break

        # Recorrer todos los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            # Calcular la distancia desde el nodo actual al vecino
            distancia_alternativa = distancias[nodo_actual] + peso

            # Si la distancia alternativa es menor que la distancia registrada
            if distancia_alternativa < distancias[vecino]:
                # Actualizar la distancia
                distancias[vecino] = distancia_alternativa
                # Guardar el predecesor para reconstruir el camino
                predecesores[vecino] = nodo_actual
                # Añadir el vecino a la cola de prioridad con la nueva distancia
                heapq.heappush(cola_prioridad, (distancia_alternativa, vecino))

    # Reconstruir el camino desde el fin hasta el inicio
    camino = []
    nodo_actual = fin
    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = predecesores.get(nodo_actual, None)

    # Invertir el camino para obtener el orden correcto
    camino.reverse()

    # Obtener el costo del camino
    costo = distancias[fin]

    return camino, costo


# Definición del grafo
grafo = {
    '1': {'2': 3, '3': 6},
    '2': {'1': 3, '3': 2, '4': 1},
    '3': {'1': 6, '2': 2, '4': 4, '5': 2},
    '4': {'2': 1, '3': 4, '5': 6},
    '5': {'3': 2, '4': 6, '6': 2, '7': 2},
    '6': {'5': 2, '7': 3},
    '7': {'5': 2, '6': 3}
}

# EL camino mas corto
camino, costo = dijkstra(grafo, '1', '7')

# Da el resultado
print(f"El camino más corto es: {camino} con un costo de: {costo}")
