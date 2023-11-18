# 4. Invertir una lista
# Escribe una función que invierta una lista dada.

lista = ['uno', 2, 3.0, ['cuatro', 5], True]

def invertir(listas):
    lista_inversa = []
    contador = 1
    while len(lista_inversa) < len(listas):
        lista_inversa.append(listas[-contador])
        contador +=1
    return(lista_inversa)

print(invertir(lista))

# print(lista[2])

