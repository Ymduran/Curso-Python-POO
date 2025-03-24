print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Bug fixes                                                        * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")

"""
Se supone que el método elimina los números pares de la lista y devuelve una lista que contiene los números impares.
Sin embargo, hay un error en el método que debe solucionarse.
Función original.

def kata_13_december(lst): 
    # Fix this code
    for i in range(len(lst)): 
        if lst[i]%2==0: 
            lst.remove(i)
    return lst
"""
#Función corregida
def kata_13_december(lst: list) -> list:
    """
    Esta función ahora guarda los pares en una lista auxiliar, al parecer el error era que modificaba la
    cantidad de elementos de la lista, y sucede que al eliminar algún elemento, el resto de la iteración quedaba
    fuera de rango.
    :param lst: Lista de número pares e impares
    :return: Una lista con todos los números impares
    """
    # Fix this code
    lst_aux = []
    for i in range(len(lst)):
        if (lst[i] % 2 ) != 0:
            lst_aux.append(lst[i])
    return lst_aux

if __name__ == '__main__':
    print(kata_13_december([1, 2, 2, 2, 4, 3, 4, 5, 6, 7]))
    print(kata_13_december([1, 2, 2, 2, 4, 3, 4]))