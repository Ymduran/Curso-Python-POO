print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 13 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Create a function that finds the integral of the expression passed.*                                        * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")
import unittest


def integrate(coefficient: int, exponent:int) -> str:
    """
    :param coefficient: De tipo entero
    :param exponent: De tipo entero
    :return: Una cadena que muestra la integral
    """
    return f'{coefficient // (exponent + 1)}x^{exponent + 1} '

if __name__ == '__main__':
    print(integrate(3, 2))
    print(integrate(20, 1))








