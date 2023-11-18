# # 9. Pila de historial de navegación
# # Implementa una pila para simular el historial de navegación de un navegador web. 
# # Escribe funciones para agregar una nueva página y avanzar a la página anterior.


lista = []

def agregar(elementos):
    
    lista.insert(0, elementos)
    return lista

def eliminar():
    lista.pop(0)
    return lista

print(agregar(1))
print(agregar(2))
print(agregar(3))
print(agregar(4))

print(eliminar())
print(eliminar())
