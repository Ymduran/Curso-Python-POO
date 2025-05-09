print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Sumar elementos de una lista                                     * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Escriba una función que reciba una lista de números y devuelva la suma de esos números.
Los números pueden ser negativos o no enteros. Si la lista está vacía, se debe retornar 0.

Ejemplos:
Entrada: [1, 5.2, 4, 0, -1]
Salida: 9.2

Entrada: []
Salida: 0

Entrada: [-2.398]
Salida: -2.398

Supuestos:
- Siempre se recibe una lista.
- Si la lista está vacía, debe retornar 0.
- Todos los elementos son números (enteros o flotantes).
"""

def sum_array(a):
    """
    Suma los elementos de una lista de números.
    :param a: Lista de números.
    :return: Suma total de los elementos. Si la lista está vacía, retorna 0.
    """

    total = 0

    for numero in a:
        total += numero

    return total


if __name__ == '__main__':
    print(sum_array([1, 5.2, 4, 0, -1]))   # 9.2
    print(sum_array([]))                  # 0
    print(sum_array([-2.398]))            # -2.398
