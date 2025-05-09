print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Elevar un número al cuadrado                                     * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Escribe una función que reciba un argumento y retorne el cuadrado del mismo.
"""

def square(n):
    """
     Eleva al cuadrado el número proporcionado.
    :param n: número a elevar.
    :return: el número elevado al cuadrado.
    """

    return n * n


if __name__ == '__main__':
    print(square(3))     # 9
    print(square(-4))    # 16
    print(square(1.5))   # 2.25
