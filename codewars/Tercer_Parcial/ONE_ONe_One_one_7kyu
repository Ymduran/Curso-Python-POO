print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Consecutivos de unos                                             * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Descripción del ejercicio:
Crear una función que reciba una lista de números (formada por ceros y unos) 
y devuelva el mayor número de 1's consecutivos que aparecen en la lista.

Ejemplos:
    consecutive_ones([1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0]) => 3
    consecutive_ones([1, 1, 0, 0, 1]) => 2
    consecutive_ones([0, 0, 0, 0, 0]) => 0
"""

def consecutive_ones(nums: list) -> int:
    """
    Esta función recorre una lista de números y cuenta la cantidad máxima de unos consecutivos.

    :param nums: Lista de enteros (formada por 0 y 1)
    :return: Número entero que representa la mayor cantidad de unos seguidos en la lista
    """
    maximos = 0     # Variable para guardar el máximo encontrado
    actual = 0      # Contador para los unos actuales

    for num in nums:
        if num == 1:
            actual += 1         # Si es 1, aumentamos el contador actual
            if actual > maximos:
                maximos = actual   # Si el actual supera al máximo, lo actualizamos
        else:
            actual = 0          # Si es 0, se rompe la cadena, reseteamos

    return maximos


# PRUEBAS DEL CÓDIGO:
if __name__ == '__main__':
    print("Prueba 1: consecutive_ones([1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0]) =>", consecutive_ones([1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0]))  # Esperado: 3
    print("Prueba 2: consecutive_ones([1, 1, 0, 0, 1]) =>", consecutive_ones([1, 1, 0, 0, 1]))                                # Esperado: 2
    print("Prueba 3: consecutive_ones([0, 0, 0, 0, 0]) =>", consecutive_ones([0, 0, 0, 0, 0]))                                # Esperado: 0
    print("Prueba 4: consecutive_ones([1, 1, 1, 1, 1]) =>", consecutive_ones([1, 1, 1, 1, 1]))                                # Esperado: 5
    print("Prueba 5: consecutive_ones([0, 1, 1, 0, 1, 1, 1, 1]) =>", consecutive_ones([0, 1, 1, 0, 1, 1, 1, 1]))              # Esperado: 4


