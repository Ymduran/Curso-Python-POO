print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Determinar si un número es par o impar                          * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Crear una función que reciba un número entero como argumento y regrese:
- "Even" si el número es par
- "Odd" si el número es impar
"""

def even_or_odd(number):
    """
    Determina si un número es par o impar.

    Parámetro:
    number (int): Número entero a evaluar.

    Retorna:
    str: "Even" si es par, "Odd" si es impar.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == '__main__':
    print(even_or_odd(4))   # Even
    print(even_or_odd(7))   # Odd
    print(even_or_odd(0))   # Even
    print(even_or_odd(-3))  # Odd
