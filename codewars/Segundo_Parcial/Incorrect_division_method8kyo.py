print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * División entre dos números con resultado decimal si es necesario * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Este método debe devolver el resultado de dividir su primer argumento entre el segundo.
La versión original usaba división entera, lo que causaba errores cuando el resultado no era exacto.

Corrección:
- Usar división normal en lugar de división entera para obtener resultados decimales cuando sea necesario.
"""

def divide_numbers(x, y):
    """
    Divide dos números y devuelve el resultado. Si el divisor es cero, muestra un mensaje de error.

    Parámetros:
    x (float/int): Número que será dividido.
    y (float/int): Número divisor.

    Retorna:
    float: Resultado de la división.
    """
    if y == 0:
        print("Error: No se puede dividir entre cero.")
        return None
    else:
        return x / y


if __name__ == '__main__':
    print(divide_numbers(10, 2))    # 5.0
    print(divide_numbers(7, 3))     # 2.333...
    print(divide_numbers(5, 0))     # Error
