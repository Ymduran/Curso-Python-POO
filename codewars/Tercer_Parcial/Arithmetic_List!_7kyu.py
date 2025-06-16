print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Generar secuencia aritmética                                     * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Descripción del ejercicio:
Crear una función que genere una secuencia aritmética dados tres parámetros:
    - first: el primer término de la secuencia
    - c: la constante que se suma en cada paso
    - l: la cantidad total de términos que debe tener la lista generada

La secuencia se forma así:
    término_0 = first
    término_1 = first + c
    término_2 = first + 2*c
    ...
    término_(l-1) = first + (l-1)*c

Ejemplo:
    seqlist(0, 1, 5) => [0, 1, 2, 3, 4]
    seqlist(2, 2, 4) => [2, 4, 6, 8]
"""

def seqlist(first: int, c: int, l: int) -> list:
    """
    Esta función genera una lista de longitud 'l' siguiendo una secuencia aritmética
    que comienza en 'first' y donde cada término se obtiene sumando la constante 'c'.

    :param first: Primer número de la secuencia
    :param c: Constante a sumar en cada paso
    :param l: Número de términos a generar
    :return: Lista de números enteros con la secuencia completa
    """
    secuencia = []
    for i in range(l):  # Iteramos desde 0 hasta l-1
        termino = first + i * c
        secuencia.append(termino)
    return secuencia


if __name__ == '__main__':
    print("Prueba 1: seqlist(0, 1, 5) =>", seqlist(0, 1, 5))     
    print("Prueba 2: seqlist(2, 2, 4) =>", seqlist(2, 2, 4))     
    print("Prueba 3: seqlist(10, -1, 5) =>", seqlist(10, -1, 5)) 
    print("Prueba 4: seqlist(5, 0, 3) =>", seqlist(5, 0, 3))   
    print("Prueba 5: seqlist(-3, 3, 4) =>", seqlist(-3, 3, 4))   



"""
Notas:

- Las secuencias aritméticas se pueden generar usando una fórmula general: término = first + i * c.
- El ciclo for con `range(l)` es muy útil para recorrer una cantidad fija de pasos, del 0 al l-1.
- No se debe confundir `range(l)` con `range(1, l)` — eso habría causado un error por un término faltante.
- También se puede usar comprensión de listas si se buscara un enfoque más compacto (aunque aquí se evita por claridad).
- Se puede trabajar con constantes negativas o cero sin complicaciones.
- Este patrón puede adaptarse fácilmente a secuencias geométricas o personalizadas.

"""
