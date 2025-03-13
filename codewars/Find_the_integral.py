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

def find_the_integral(coefficient_of_x : int, exponent: int) -> str:
    """
    :param coefficient_of_x: De tipo entero
    :param exponent: De tipo entero
    :return: Una cadena que muestra la integral
    """
    return f"∫{coefficient_of_x}x^{exponent}dx = {coefficient_of_x/(exponent+1)}^{exponent+1} + C"


if __name__ == '__main__':
    coefficient_of_x = int(input("Ingresa el coeficiente de x en número positivo: "))
    exponent = int(input("Ingresa el exponente en número positivo: "))
    print(find_the_integral(coefficient_of_x, exponent))
