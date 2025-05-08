print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Crear una matriz de m por n en forma de caja con números que    * ")
print(" * aumentan hacia el centro.                                        * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Dado dos enteros positivos `m` (ancho) y `n` (alto), se debe generar una lista de listas (matriz) con `n` filas y `m` columnas,
donde se forma un patrón de capas que incrementan desde los bordes hacia el centro.

- La capa más externa contiene puros 1.
- La siguiente capa hacia el interior contiene 2.
- Luego 3, y así sucesivamente hasta el centro.
"""

def create_box(m, n):
    # Creamos una matriz vacía de n filas por m columnas
    caja = []
    for fila in range(n):
        nueva_fila = []
        for columna in range(m):
            # Calculamos la distancia mínima a un borde (arriba, abajo, izquierda, derecha)
            distancia_arriba = fila
            distancia_abajo = n - 1 - fila
            distancia_izquierda = columna
            distancia_derecha = m - 1 - columna

            # Tomamos la menor distancia para saber el número que va
            valor = min(distancia_arriba, distancia_abajo, distancia_izquierda, distancia_derecha) + 1

            nueva_fila.append(valor)
        caja.append(nueva_fila)
    
    return caja


# Ejemplos de uso
if __name__ == '__main__':
    resultado1 = create_box(5, 8)
    for fila in resultado1:
        print(fila)

    print("\n")

    resultado2 = create_box(10, 9)
    for fila in resultado2:
        print(fila)
