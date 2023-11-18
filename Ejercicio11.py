# 11. Multiplicación de matrices
# Escribe una función que multiplique dos matrices dadas.

def multiplicar_matrices(matriz1, matriz2):
    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]

    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] = matriz1[i][j] * matriz2[i][j]
    return resultado

matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [6, 7, 8]
]

matriz_b = [
    [7, 8, 9],
    [9, 10, 11],
    [11, 12, 13],
]

resultado = multiplicar_matrices(matriz_a, matriz_b)

# Mostrar el resultado
for fila in resultado:
    print(fila)