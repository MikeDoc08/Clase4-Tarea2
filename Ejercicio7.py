# 7. Contar elementos únicos
# Escribe una función que tome una lista y devuelva la cantidad de elementos únicos en ella.

lista = [ 1, 1,'k', 2, 3, 3, 2, 'Hola', 5, 6, 7, 6, 'q', 'k']

def elementosUnicos(lists):
    i = 0
    while i < len(lists):
        j = i + 1 
        while j < len(lists):
            if lists[i] == lists[j]:
                lists.pop(j)
                lists.pop(i)
                i = 0
                j = i + 1
            else:
                j += 1
        i += 1 
    return(lists)

print(elementosUnicos(lista))
