import math
import random
from flask import Flask, render_template, jsonify

def distancia(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

# Calcular la distancia correcta por una ruta
def evalua_rutaH(ruta, coord):
    total = 0
    for i in range(0, len(ruta) - 1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    # Cierra el ciclo, regresando a la primera ciudad
    ciudad1 = ruta[-1]
    ciudad2 = ruta[0]
    total += distancia(coord[ciudad1], coord[ciudad2])
    return total

def i_hill_climbing(coord):
    # Crear ruta inicial aleatoria
    ruta = list(coord.keys())
    mejor_ruta = ruta[:]
    max_iteraciones = 10

    while max_iteraciones > 0:
        mejora = True
        # Generar nueva ruta aleatoria
        random.shuffle(ruta)
        while mejora:
            mejora = False
            dist_actual = evalua_rutaH(ruta, coord)
            # Evaluar a los vecinos
            for i in range(0, len(ruta) - 1):
                if mejora:
                    break
                for j in range(i + 1, len(ruta)):
                    ruta_tmp = ruta[:]
                    # Intercambiar ciudades
                    ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                    dist = evalua_rutaH(ruta_tmp, coord)
                    if dist < dist_actual:
                        mejora = True
                        ruta = ruta_tmp[:]
                        dist_actual = dist
                        break

        max_iteraciones -= 1

        if evalua_rutaH(ruta, coord) < evalua_rutaH(mejor_ruta, coord):
            mejor_ruta = ruta[:]

    return mejor_ruta

coordH = {
        'Jiloyork': (19.916012, -99.580580),
        'Toluca': (19.289165, -99.655697),
        'Atlacomulco': (19.799520, -99.873844),
        'Guadalajara': (20.677754472859146, -103.34625354877137),
        'Monterrey': (25.69161110159454, -100.321838480256),
        'QuintanaRoo': (21.163111924844458, -86.80231502121464),
        'Michoacan': (19.701400113725654, -101.20829680213464),
        'Aguascalientes': (21.87641043660486, -102.26438663286967),
        'CDMX': (19.432713075976878, -99.13318344772986),
        'QRO': (20.59719437542255, -100.38667040246602),
}


#print("Ruta:", ruta)
#print("Distancia Total:", evalua_ruta(ruta, coord))

