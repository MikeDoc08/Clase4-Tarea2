# 8. Comprobación de palíndromos
# Escribe una función que verifique si una palabra dada es un palíndromo.

from Ejercicio4 import invertir

def palindromo(cadena):

    i = cadena

    if isinstance(cadena, int):
        cadena_list = [int(digito) for digito in str(i)]
    else:
        cadena_list = list(cadena)
    
    cadena_inversa = invertir(cadena_list)

    if cadena_list == cadena_inversa:
        return True
    else:
        return False

prueba1 = 'radar'
prueba2 = 'reconocer'
prueba3 = 122
prueba4 = 13331 

print(palindromo(prueba1))
print(palindromo(prueba2))
print(palindromo(prueba3))
print(palindromo(prueba4))