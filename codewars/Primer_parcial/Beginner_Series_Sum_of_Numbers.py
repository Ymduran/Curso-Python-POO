print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Suma de series de números                                        * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")
"""
Dados dos números enteros a y b, que pueden ser positivos o negativos,
calcula la suma de todos los números enteros entre ellos (incluyéndolos) y devuélvela.
Si los dos números son iguales, devuelve a o b.
Nota: ¡a y b no están ordenados!
"""
def get_sum(a: int,b:int )-> int:
    """
    Esta función retorna la suma de series de dos números, para lo cuál debe determinar primero cuál es el mayor y cuál es el menor
    esto lo puedo hacer con las palabras reservadas max y min, que tiene como "argumento" ambos números y posteriormente determina
    cuál es el mayor y cuál es el menor respectivamente.
    Utilizo la formula de la suma de la serie.
    :param a: primer número
    :param b: segundo número
    :return: retorna la suma de la serie si son iguales y de ser iguales retorna cuálquiera de los dos, en este caso decido a.
    """

    mayor, menor = max(a,b), min(a,b)
    if a != b:
        return (mayor * (mayor +1)//2) - ((menor -1) * menor //2) #Fórmulla de la suma de una serie aritmética
    else:
        return a



if __name__ == '__main__':
    print(get_sum(0,1))
    print(get_sum(1, 1))
    print(get_sum(-30, -30))
    print(get_sum(-434, 1172))
    print(get_sum(-4977,-2640))



