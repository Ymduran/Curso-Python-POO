print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Suma de binarios                                                 * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")
"""
El Club de Croquet de los Suburbios Occidentales ofrece dos categorías de membresía:
 Senior y Abierta. Solicitan su ayuda con un formulario de solicitud que indicará a los futuros miembros en qué categoría se les asignará.
Para ser senior, un miembro debe tener al menos 55 años y un hándicap superior a 7. 
En este club de croquet, los hándicaps van de -2 a +26; cuanto mejor sea el jugador, menor será el hándicap.
Entrada
La entrada consistirá en una lista de pares. 
Cada par contiene la información de un posible miembro. 
La información consiste en un entero para la edad de la persona y un entero para su hándicap.
Salida
La salida consistirá en una lista de valores de cadena (en Haskell y C: Abierta o Senior) que indica si el miembro 
correspondiente se asignará a la categoría senior o abierta.
"""

def open_or_senior(data:list) -> list:
    """
    Esta Función compara cada tupla de la lista (primer con el segundo elemento) y evalúa las condiciones para determinar
    si pertenece a Senior o Open
    :param data: Lista de tuplas
    :return: Lista
    """
    list = []
    for i in range (len(data)):
        if data[i][0] >= 55 and data[i][1] > 7:
            #print(data[i][1])
            list.append('Senior')
        else:

            list.append('Open')

    return list


if __name__ == '__main__':
    print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
    print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
