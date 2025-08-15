# 1. Determina cuales son los indices donde aparece patron en cadena 
#    usando comparaciones entre caracteres unitarios. 
#    La salida correcta deberia ser 10 y 15. Tu codigo debe averiguarlo. 
# 2. Que complejidad tiene el algoritmo? 

#complejidad O(n*m) n es la longitud de la cadena y m es la longitud del patrón 

cadena = "this is a small example"
patron = "small"

print("Buscando: ", patron)
print("Dentro de: ", cadena)

print( patron[0] == cadena[0] ) # <--- ejemplo de comparacion entre caracteres

def buscar_patron(cadena, patron):
    indices = []
    for i in range(len(cadena) - len(patron) + 1):
        encontrado = True
        for j in range(len(patron)):
            if cadena[i + j] != patron[j]:
                encontrado = False
                break
        if encontrado:
            indices.append(i)
    return indices

print(buscar_patron(cadena, patron))