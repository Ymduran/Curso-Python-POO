print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Convertir número entero a número romano                          * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Cree una función que reciba un número entero positivo entre 1 y 3999 (incluidos ambos)
y devuelva una cadena que contenga su representación en números romanos.

Los números romanos modernos se escriben expresando cada dígito por separado desde el más a la izquierda,
y omitiendo cualquier dígito con valor cero. No puede haber más de tres símbolos idénticos seguidos.

Ejemplos:
1990 se representa como: 1000=M + 900=CM + 90=XC → MCMXC
2008 se escribe como: 2000=MM + 8=VIII → MMVIII
1666 usa todos los símbolos romanos en orden descendente → MDCLXVI

Guía de símbolos:
I → 1
V → 5
X → 10
L → 50
C → 100
D → 500
M → 1000
"""

def solution(n):
    """
    convierte un número entero entre 1 y 3999 a su forma en números romanos.
    :param n: n (int): Número entero entre 1 y 3999.
    :return: str: Cadena con el número romano correspondiente.
    """

    numeros = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    resultado = ''

    for valor, simbolo in numeros:
        while n >= valor:
            resultado += simbolo
            n -= valor

    return resultado


if __name__ == '__main__':
    print(solution(1))       # I
    print(solution(1000))    # M
    print(solution(1990))    # MCMXC
    print(solution(2008))    # MMVIII
    print(solution(1666))    # MDCLXVI
