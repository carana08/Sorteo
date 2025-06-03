import random as rd

def sorteo(lista1, lista2):
    diccionario = {}
    primera_eleccion_aleatoria = rd.randint(0, len(lista1) - 1)
    segunda_eleccion_aleatoria = rd.randint(0, len(lista2) - 1)
    diccionario.update({lista1[primera_eleccion_aleatoria]: lista2[segunda_eleccion_aleatoria]})
    
    return lista1[numero_aleatorio], lista2[numero_aleatorio]

print(sorteo())