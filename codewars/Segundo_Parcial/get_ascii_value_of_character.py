print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Obtener el valor ASCII de un carácter usando lógica propia       * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Escribe una función que reciba un carácter y retorne su valor ASCII
sin usar funciones especiales como ord().
La tabla ASCII tiene valores numéricos asignados a cada carácter.
Esta función calcula ese valor leyendo directamente desde una cadena ordenada.
"""

def get_ascii(ch: str) -> int:
    """
    Calcula el valor ASCII del carácter recibido sin usar ord().

    Parámetro:
    ch (str): Un solo carácter.

    Retorna:
    int: Valor ASCII del carácter.
    """
    caracteres = ""
    for i in range(128):
        caracteres += chr(i)

    posicion = -1
    for i in range(len(caracteres)):
        if caracteres[i] == ch:
            posicion = i
            break

    return posicion


if __name__ == '__main__':
    print(get_ascii('A'))  # 65
    print(get_ascii('a'))  # 97
    print(get_ascii('!'))  # 33
    print(get_ascii(' '))  # 32
