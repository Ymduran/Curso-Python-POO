"""
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any char.
"""
def xo(s:str) -> bool:
    """
    Esta función determina si en la cadena existen las mismas cantidades de "o"s que de "x"s,
    esto con un contador, que itera en la función, finalmente sí son la misma cantidad retorna un booleano.
    :param s: Una cadena de letras
    :return: Un booleano que compara si ambos contadores son iguales
    """
    countx, counts  = 0, 0
    for leter in s:
        if leter.lower() == "x": countx += 1
        if leter.lower() == "o": counts += 1
    return (countx == counts)

if __name__ == '__main__':
    print(xo("xxoo"))
    print(xo("xOxXo"))

