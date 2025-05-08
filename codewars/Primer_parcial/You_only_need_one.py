print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 26 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Create a function that finds the integral of the expression passed.* ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")
"""
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
a can contain numbers or strings. x can be either.
Return true if the array contains the value, false if not.

"""

def check(seq: list , elem: int or str) -> bool:
    """
    Esta función evalúa sí dentro de la lista existe algún segundo elemento
    :param seq: Una lista de números o caracteres
    :param elem: Un elemento de tipo entero o cadena
    :return: Retorna un valor booleano, True si elemento está entre la lista o False si no.
    """
    if elem in seq:
        return True
    else:
        return False






if __name__ == '__main__':
    print(check([66, 101], 66))
    print(check([78, 117, 110, 99, 104, 117, 107, 115], 8))
    print(check(["what", "a", "great", "kata"], "kat"))
