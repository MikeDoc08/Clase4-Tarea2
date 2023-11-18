# 6. Cola de tareas
# Implementa una cola de tareas utilizando una lista. 
# Escribe funciones para agregar una tarea y eliminar la tarea más antigua.

lista = []

def agregar(tarea):
    lista.append(tarea)
    print(f'La Tarea: {tarea} fue agregada')

def eliminar():
    print(f'La Tarea: {lista[0]} fue eliminada')
    lista.pop(0)

agregar('Tarea 1')
print(lista)
agregar('Tarea 2')
print(lista)
agregar('Tarea 3')
print(lista)
agregar('Tarea 4')
print(lista)
agregar('Tarea 5')
print(lista)
agregar('Tarea 6')
print(lista)

print(lista)

eliminar()
print(lista)
eliminar()
print(lista)
eliminar()
print(lista)
eliminar()
print(lista)

