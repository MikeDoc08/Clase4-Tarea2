# 5. Validación de paréntesis
# Escribe una función que tome una cadena que contiene paréntesis y verifique si están balanceados.

def paréntesis_balanceados(cadena):
    pila = []
    parejas = {')': '(', '}': '{', ']': '['}

    for caracter in cadena:
        if caracter in parejas.values():
            pila.append(caracter)
        elif caracter in parejas.keys():
            if pila and pila[-1] == parejas[caracter]:
                pila.pop()
            else:
                return False
    return not pila

# Ejemplo de uso
cadena1 = "([()])"
cadena2 = "{[()]}"
cadena3 = "(()))"

print(paréntesis_balanceados(cadena1))
print(paréntesis_balanceados(cadena2))
print(paréntesis_balanceados(cadena3))