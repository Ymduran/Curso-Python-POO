print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 01 junio del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Retornar cadena con número con ceros a la izquierda              * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Descripción del ejercicio:
Completar una función que devuelva una cadena con el siguiente formato:
    "Value is 00005"
Donde el número recibido debe estar formateado para que tenga 5 dígitos, rellenando con ceros a la izquierda si es necesario.

Ejemplo:
    solution(5) => "Value is 00005"
    solution(42) => "Value is 00042"
    solution(12345) => "Value is 12345"
"""

def solution(value: int) -> str:
    """
    Esta función convierte un número entero a una cadena con el formato:
    "Value is XXXXX" donde XXXXX es el número con ceros a la izquierda (5 dígitos).

    :param value: Número entero a formatear
    :return: Cadena con el formato solicitado
    """
    numero_formateado = str(value).zfill(5)  # zfill completa con ceros hasta tener 5 caracteres
    return f"Value is {numero_formateado}"



if __name__ == '__main__':
    print("Prueba 1:", solution(5))       
    print("Prueba 2:", solution(42))    
    print("Prueba 3:", solution(123))
    print("Prueba 4:", solution(9999))    
    print("Prueba 5:", solution(12345))  
    print("Prueba 6:", solution(0))     

"""

"""
