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

def integrate(coefficient, exponent) -> str:
    """
    :param coefficient_of_x: De tipo entero
    :param exponent: De tipo entero
    :return: Una cadena que muestra la integral
    """
    return f"∫{coefficient}x^{exponent}dx = {coefficient / (exponent + 1)}^{exponent + 1} + C"



def basic_tests() -> None:
    """

    :return:
    """
    test.assert_equals(integrate(3, 2), "1x^3")
    test.assert_equals(integrate(12, 5), "2x^6")
    test.assert_equals(integrate(20, 1), "10x^2")
    test.assert_equals(integrate(40, 3), "10x^4")
    test.assert_equals(integrate(90, 2), "30x^3")



if __name__ == '__main__':
    basic_tests()



