# 1. Determina cuales son los dos puntos mas cercanos dadas sus coordenadas x, y
#complejidad O(n^2) debido a que se utilizan dos bucles anidados para calcular la distancia entre todos los pares de puntos

import math

coor = [[-2.423, -8.469],
[5.721,	9.354],
[6.766,	-3.823],
[4.129,	6.744],
[5.371,	-5.404]]




def distancia(p1, p2):
    return math.sqrt(math.pow((p1[0] - p2[0]), 2) + math.pow((p1[1] - p2[1]), 2))
def puntos_mas_cercanos(coordenadas):
    punto1 = coordenadas[0]
    punto2 = coordenadas[1]
    min_dist = distancia(punto1, punto2)
    for i in range(len(coordenadas)):
        for j in range(i + 1, len(coordenadas)):
            dist = distancia(coordenadas[i], coordenadas[j])
            if dist < min_dist:
                min_dist = dist
                punto1 = coordenadas[i]
                punto2 = coordenadas[j]
    
    return punto1, punto2, min_dist

p1, p2, dist = puntos_mas_cercanos(coor)
print("Puntos más cercanos:", p1, p2)
print("Distancia:", dist)



