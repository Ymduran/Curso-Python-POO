print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Convertir una lista en una cadena separada por comas            * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Entrada: Una lista de elementos (números, cadenas, booleanos, listas, etc.)

Ejemplo:
Entrada: ["h", "o", "l", "a"]
Salida: "h,o,l,a"

Se debe retornar una cadena con los elementos separados por comas, en el mismo orden.
Todos los elementos deben convertirse en texto antes de unirlos.
"""

def print_array(arr):
    """
    Une los elementos de una lista en una cadena separada por comas.
    :param arr: Lista de cualquier tipo de datos.
    :return: Cadena con los elementos separados por comas.
    """

    resultado = ""
    
    for i in range(len(arr)):
        elemento = str(arr[i])
        resultado += elemento
        if i < len(arr) - 1:
            resultado += ","
    
    return resultado


if __name__ == '__main__':
    print(print_array(["h", "o", "l", "a"]))        # h,o,l,a
    print(print_array([1, 2, 3]))                   # 1,2,3
    print(print_array([True, False, True]))         # True,False,True
    print(print_array([[1, 2], [3, 4]]))            # [1, 2],[3, 4]
