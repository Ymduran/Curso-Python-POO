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
"""
Crea una función que encuentre la integral de la expresión pasada.
Para encontrar la integral, solo necesitas sumar uno al exponente (el segundo argumento) 
y dividir el coeficiente (el primer argumento) entre ese nuevo número.
Por ejemplo, para 3x^2, la integral sería 1x^3: sumamos uno al exponente y 
dividimos el coeficiente entre ese nuevo número.
Notas:
La salida debe ser una cadena.
El coeficiente y el exponente siempre son un entero positivo.
"""

def integrate(coefficient: int, exponent:int) -> str:
    """
    Esta Función muestra en formato de str la integral
    :param coefficient: De tipo entero
    :param exponent: De tipo entero
    :return: Una cadena que muestra la integral
    """
    return f'{coefficient // (exponent + 1)}x^{exponent + 1} '

if __name__ == '__main__':
    print(integrate(3, 2))
    print(integrate(20, 1))








