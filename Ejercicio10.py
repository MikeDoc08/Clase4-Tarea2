# 10. Diccionario de frecuencia
# Escribe una función que tome una lista y devuelva un diccionario que muestre la frecuencia de cada elemento en la lista.

def frecuencia_elementos(lista):
    frecuencia = {}
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1

    for elemento, cantidad in frecuencia.items():
        print(f'{elemento}: {cantidad} veces')

mi_lista = ['Hola', 2, 3, 1, 2, 3, 1, 2, 1, 4]

frecuencia_elementos(mi_lista)
