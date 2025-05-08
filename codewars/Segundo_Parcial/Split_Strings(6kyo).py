print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Separar cadena en pares de dos caracteres                        * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Complete la función para que divida la cadena en pares de dos caracteres.
Si la cadena contiene un número impar de caracteres, entonces se debe agregar un guion bajo ('_')
como segundo carácter del último par.

Ejemplos:

'abc' => ['ab', 'c_']
'abcdef' => ['ab', 'cd', 'ef']
"""

def solution(s):
    """
    Divide una cadena en pares de dos caracteres. Si la cantidad de caracteres es impar,
    el último par se completa con un guion bajo.

    Parámetro:
    s (str): La cadena de entrada.

    Retorna:
    list: Lista con pares de caracteres.
    """
    resultado = []
    i = 0

    while i < len(s):
        if i + 1 < len(s):
            resultado.append(s[i] + s[i + 1])
        else:
            resultado.append(s[i] + '_')
        i += 2

    return resultado


if __name__ == '__main__':
    print(solution('abc'))       # ['ab', 'c_']
    print(solution('abcdef'))    # ['ab', 'cd', 'ef']
    print(solution('a'))         # ['a_']
    print(solution(''))          # []
