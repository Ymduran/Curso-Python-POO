print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 15 de junio  del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Codificador y decodificador de vocales a números                 * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Instrucciones:
Paso 1:
Crear una función llamada `encode()` que reemplace las vocales minúsculas en una cadena 
con los siguientes números:
a → 1, e → 2, i → 3, o → 4, u → 5

Ejemplo: encode("hello") → "h2ll4"

Paso 2:
Crear una función llamada `decode()` que convierta los números 1-5 en sus respectivas 
vocales, usando la misma tabla anterior.

Ejemplo: decode("h3 th2r2") → "hi there"
"""

def encode(st: str) -> str:
    """
    Reemplaza las vocales a, e, i, o, u por 1, 2, 3, 4, 5 respectivamente.
    :param st: Cadena a codificar
    :return: Cadena codificada
    """
    # Diccionario de reemplazo
    tabla = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    resultado = ""

    # Recorremos cada carácter de la cadena
    for letra in st:
        if letra in tabla:
            resultado += tabla[letra]
        else:
            resultado += letra

    return resultado


def decode(st: str) -> str:
    """
    Reemplaza los números 1-5 por las vocales correspondientes.
    :param st: Cadena a decodificar
    :return: Cadena original con vocales
    """
    # Diccionario inverso
    tabla = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    resultado = ""

    # Recorremos cada carácter de la cadena
    for letra in st:
        if letra in tabla:
            resultado += tabla[letra]
        else:
            resultado += letra

    return resultado



if __name__ == '__main__':
    print(encode("hello"))          # h2ll4
    print(encode("hi there"))       # h3 th2r2
    print(encode("a quick brown fox"))  # 1 q53ck br4wn f4x

    print(decode("h3 th2r2"))       # hi there
    print(decode("h2ll4"))          # hello
    print(decode("1 q53ck br4wn f4x"))  # a quick brown fox
