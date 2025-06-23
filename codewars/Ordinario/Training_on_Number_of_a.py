print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 23 de junio del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Contar pares únicos de anagramas en una lista de palabras       * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Instrucciones:
Un anagrama es una palabra formada reorganizando las letras de otra palabra.
Por ejemplo: "angel" y "glean".

Crear una función que reciba una lista de palabras y devuelva el total de
pares distintos de palabras que sean anagramas entre sí.

Ejemplos:
anagram_counter(["dell", "ledl", "abc", "cba"]) → 2
anagram_counter(["dell", "ledl", "abc", "cba", "bca", "bac"]) → 7
"""

def anagram_counter(words: list) -> int:
    """
    Cuenta cuántos pares únicos de palabras en la lista son anagramas.

    :param words: Lista de palabras (strings).
    :return: Número total de pares de anagramas.
    """
    from collections import defaultdict

    #Creamos un diccionario para agrupar por "firma" de letras ordenadas
    grupos = defaultdict(list)

    for palabra in words:
        clave = ''.join(sorted(palabra))
        grupos[clave].append(palabra)

    # Para cada grupo de palabras anagramas, contar las combinaciones posibles de pares
    total_pares = 0
    for lista in grupos.values():
        n = len(lista)
        if n > 1:
            #Fórmula de combinaciones: C(n, 2) = n(n-1)/2
            total_pares += (n * (n - 1)) // 2

    return total_pares


if __name__ == '__main__':
    print(anagram_counter(["dell", "ledl", "abc", "cba"]))                        # 2
    print(anagram_counter(["dell", "ledl", "abc", "cba", "bca", "bac"]))          # 7
    print(anagram_counter(["abc", "def", "ghi"]))                                 # 0
    print(anagram_counter(["a", "a", "a"]))                                       # 3
    print(anagram_counter(["listen", "silent", "enlist", "google", "gogole"]))   # 4


"""
Para detectar si dos palabras son anagramas, se ordenan sus letras, Si son iguales, son anagramas.
Se agrupan las palabras en un diccionario usando la "firma" (palabra ordenada) como clave.
Se cuentan los pares posibles en cada grupo con la fórmula de combinaciones:
𝐶(𝑛,2)=𝑛(𝑛−1)2C(n,2)= 2n(n−1)
Esta lógica evita repetir pares como (a, b) y (b, a).
"""
