print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 26 mayo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Detección de operación matemática                                * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Descripción del ejercicio:
Se debe crear una función que reciba 3 números: dos operandos (a, b) y un resultado.
La función debe devolver una cadena que indique qué operación matemática se usó para obtener ese resultado:
    "addition", "subtraction", "multiplication" o "division".

Ejemplos:
    operation(1, 2, 3) => "addition"       # 1 + 2 = 3
    operation(5, 2, 2.5) => "division"     # 5 / 2 = 2.5

Notas:
- No hay divisiones entre cero.
- Siempre hay una sola operación correcta.
"""

def calc_type(a: float, b: float, result: float) -> str:
    """
    Esta función determina qué operación entre a y b produce el resultado dado.

    :param a: Primer número (operando)
    :param b: Segundo número (operando)
    :param result: Resultado esperado de alguna operación entre a y b
    :return: Una cadena con el nombre de la operación usada
    """
    if a + b == result:
        return "addition"
    elif a - b == result:
        return "subtraction"
    elif a * b == result:
        return "multiplication"
    elif a / b == result:
        return "division"
    else:
        return "unknown"  # Nunca debería pasar, pero por seguridad


if __name__ == '__main__':
    print("Prueba 1: calc_type(1, 2, 3) =>", calc_type(1, 2, 3))           #  "addition"
    print("Prueba 2: calc_type(5, 2, 3) =>", calc_type(5, 2, 3))           #"subtraction"
    print("Prueba 3: calc_type(3, 4, 12) =>", operation(3, 4, 12))         #  "multiplication"
    print("Prueba 4: calc_type(5, 2, 2.5) =>", operation(5, 2, 2.5))       # "division"
    print("Prueba 5: calc_type(10, 10, 20) =>", operation(10, 10, 20))     #  "addition"


