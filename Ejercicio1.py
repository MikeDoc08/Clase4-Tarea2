# 1. Suma de elementos en una lista
# Escribe una función que reciba una lista de números y devuelva la suma de todos los elementos.

def sumarLista(listas):
    resultado = 0
    for elemento in listas:
        resultado += elemento
    print(resultado)

sumarLista([1, 2, 3, 4, 5, 6])