print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Suma de binarios                                                 * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")
"""
Implemente una función que sume dos números y devuelva su suma en binario. 
La conversión puede realizarse antes o después de la suma.
El número binario devuelto debe ser una cadena.
"""
def add_binary(a: int,b:int) -> str:
    """
    Esta función suma dos números a y b, para después convertirlos a binario; la conversión lo hace uniendo a una lista 0 si el
    residuo de la división es 0 y un 1 si es diferetente, eventualmente invertirá esa lista
    :param a: Primer número Entero
    :param b: Segundo número Entero.
    :return: Retorna una cadena. Lista invertida, separando cada elemento con un espació.
    """
    suma = a + b
    lista = []
    while suma > 0:
        if suma % 2 == 0:
            lista.append("0")
        else:
            lista.append("1")
        suma = suma // 2

    return ''.join(lista[::-1])





if __name__ == '__main__':
    print(add_binary(1, 1))
    print(add_binary(2, 2))
    print(add_binary(51, 12))