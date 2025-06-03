import random as rd

def sorteo(lista1, lista2):
    diccionario = {}
    for i in range(len(lista1)):
        primera_eleccion_aleatoria = rd.randint(0, len(lista1) - 1)
        segunda_eleccion_aleatoria = rd.randint(0, len(lista2) - 1)
        diccionario.update({lista1[primera_eleccion_aleatoria]: lista2[segunda_eleccion_aleatoria]})
        lista1.pop(primera_eleccion_aleatoria)
        lista2.pop(segunda_eleccion_aleatoria)
    return diccionario

print(sorteo(['Jose', 'Juan', 'Carlos'], ['250', '78', '90']))