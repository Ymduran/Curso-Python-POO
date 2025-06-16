print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha:  10 junio del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Verificar si dos tableros de poker son isomorfos                 * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Descripción del ejercicio:
En póker, dos tableros (conjuntos de cartas) son isomorfos si se puede hacer un mapeo uno a uno entre los palos
de modo que al aplicar ese mapeo a las cartas del primer tablero se obtenga el segundo.

- Cada carta es un par: Rango (2-9, T, J, Q, K, A) seguido por Palo (c, d, h, s).
- No importa el orden de las cartas en cada string.
- El mapeo debe ser consistente. Es decir, si 'c' → 'd', entonces todas las 'c' deben volverse 'd'.

Ejemplos:
    boards_isomorphic("AcAh2h", "AsAd2d") => True
    boards_isomorphic("AcAh2h", "AsAd2c") => False
"""

def boards_isomorphic(board1: str, board2: str) -> bool:
    """
    Determina si dos tableros de cartas son isomorfos, es decir, si existe una correspondencia
    uno a uno entre los palos que permita transformar el primero en el segundo.

    :param board1: Primer tablero de cartas (string)
    :param board2: Segundo tablero de cartas (string)
    :return: True si son isomorfos, False en caso contrario
    """
    if len(board1) != len(board2):
        return False  # No pueden ser isomorfos si tienen diferente número de caracteres (cartas)

    # Paso 1: Separar las cartas (cada carta tiene 2 caracteres: rank + suit)
    def dividir_cartas(board):
        return sorted([board[i:i+2] for i in range(0, len(board), 2)])

    cartas1 = dividir_cartas(board1)
    cartas2 = dividir_cartas(board2)

    # Paso 2: Crear correspondencia entre palos
    mapa = {}
    mapa_inverso = {}

    for c1, c2 in zip(cartas1, cartas2):
        rango1, palo1 = c1[0], c1[1]
        rango2, palo2 = c2[0], c2[1]

        # El rango debe coincidir
        if rango1 != rango2:
            return False

        # Revisar si ya existe mapeo previo
        if palo1 in mapa:
            if mapa[palo1] != palo2:
                return False  # Inconsistencia en el mapeo
        else:
            if palo2 in mapa_inverso:
                return False  # No puede haber dos palos que mapeen al mismo
            mapa[palo1] = palo2
            mapa_inverso[palo2] = palo1

    return True


# PRUEBAS DEL CÓDIGO:
if __name__ == '__main__':
    print("Prueba 1:", boards_isomorphic("AcAh2h", "AsAd2d"))  # True
    print("Prueba 2:", boards_isomorphic("AcAh2h", "AsAd2c"))  # False
    print("Prueba 3:", boards_isomorphic("Ac9d", "9hAs"))      # True (orden no importa)
    print("Prueba 4:", boards_isomorphic("As9sJs5s4s", "Ac9cJc5c4c"))  # True
    print("Prueba 5:", boards_isomorphic("AsAh", "Ac"))        # False (diferente longitud)
    print("Prueba 6:", boards_isomorphic("", ""))              # True (vacíos son isomorfos)
    print("Prueba 7:", boards_isomorphic("AcKcQc", "AdKdQd"))  # True
    print("Prueba 8:", boards_isomorphic("AcKcQc", "AdKdQs"))  # False (Q cambia de palo)


"""
Notas:

- Los tableros deben tener el mismo número de cartas (es decir, misma longitud en caracteres y múltiplo de 2).
- El uso de `zip()` permite comparar dos listas al mismo tiempo (como emparejar cartas de ambos tableros).
- Es fundamental verificar que el mapeo sea **uno a uno**: usamos un diccionario para llevar la relación
  y otro inverso para evitar que dos claves apunten al mismo valor.
- La función `sorted()` nos ayuda a ignorar el orden original de las cartas, haciendo comparaciones más fáciles.
- Este tipo de problema es común en isomorfismo de grafos o estructuras que requieren mapeo consistente.

"""
