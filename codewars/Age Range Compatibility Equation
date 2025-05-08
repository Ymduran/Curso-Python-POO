print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Calcular el rango de edad recomendable para citas                * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Todo el mundo conoce la clásica regla para las citas: "la mitad de tu edad más siete" para obtener la edad mínima recomendada.
La edad máxima se obtiene con la fórmula: (edad - 7) * 2.

Sin embargo, esta regla no se aplica cuando la edad es 14 o menor. En ese caso se usa:
mínimo = edad - 10% de edad
máximo = edad + 10% de edad

Las respuestas deben redondearse hacia abajo (sin decimales) y mostrarse en el formato: "mínimo-máximo".
"""

def dating_range(age):
    """
    Calcula el rango de edad recomendable para citas.

    Parámetro:
    age (int): Edad de la persona (entre 1 y 100).

    Retorna:
    str: Rango de edad en formato "mínimo-máximo".
    """
    if age <= 14:
        minimo = int(age - (age * 0.10))
        maximo = int(age + (age * 0.10))
    else:
        minimo = int(age / 2 + 7)
        maximo = int((age - 7) * 2)

    return str(minimo) + "-" + str(maximo)


if __name__ == '__main__':
    print(dating_range(27))   # 20-40
    print(dating_range(5))    # 4-5
    print(dating_range(17))   # 15-20
