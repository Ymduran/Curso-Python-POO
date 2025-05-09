print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 07 de mayo del 2025                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Decodificar mensaje invirtiendo el alfabeto                      * ")
print(" * Cada letra se cambia por su reflejo en el alfabeto.              * ")
print(" * Por ejemplo, a <-> z, b <-> y, c <-> x, etc.                     * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Función: decode(message)
Descripción:
Convierte un mensaje codificado invirtiendo cada letra en el alfabeto.
El mensaje solo contiene letras minúsculas y espacios.
"""

def decode(message: str):
    """
    Decodifica un mensaje donde cada letra es sustituida por su reflejo en el alfabeto.
    :param: message (str): El mensaje codificado en minúsculas y con espacios.
    :return: str: El mensaje decodificado.
    """

    alfabeto_original = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_invertido = "zyxwvutsrqponmlkjihgfedcba"
    resultado = ""

    i = 0
    while i < len(message):
        caracter = message[i]

        if caracter == " ":
            resultado = resultado + " "
        else:
            j = 0
            while j < len(alfabeto_original):
                if caracter == alfabeto_original[j]:
                    resultado = resultado + alfabeto_invertido[j]
                    break
                j = j + 1

        i = i + 1

    return resultado


# Pruebas
if __name__ == '__main__':
    print(decode("r slkv mlylwb wvxlwvh gsrh nvhhztv"))
    print(decode("zgyzhs rh ufm"))  # "attack is fun"
    print(decode("abc xyz"))        # "zyx cba"
