print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 16 de junio del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Buscar números cúbicos en cadenas y sumarlos si existen         * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Instrucciones:

Encontrar números enteros no negativos de **máximo 3 dígitos** en una cadena.
Un número es cúbico si la suma del cubo de sus dígitos es igual a sí mismo.

Ejemplo:
153 → 1³ + 5³ + 3³ = 153 → cúbico

Pasos:
1. Extraer grupos de hasta 3 dígitos seguidos de izquierda a derecha.
   Ej: "24172410" → ["241", "724", "10"]
2. Verificar si esos números son cúbicos.
3. Si hay al menos uno, retornar: "num1 num2 ... suma Lucky"
4. Si no hay ninguno, retornar: "Unlucky"
"""

def is_sum_of_cubes(s: str) -> str:
    """
    Revisa una cadena y encuentra números cúbicos de hasta 3 dígitos,
    sumándolos si existen.
    :param s: Cadena con caracteres y números mezclados.
    :return: Cadena con números cúbicos encontrados y su suma, o "Unlucky".
    """
    import re

    # Encontrar secuencias de dígitos
    bloques = re.findall(r'\d+', s)
    candidatos = []

    # Dividir bloques largos en grupos de máximo 3 cifras
    for grupo in bloques:
        for i in range(0, len(grupo), 3):
            subgrupo = grupo[i:i+3]
            if subgrupo:
                candidatos.append(subgrupo)

    # Evaluar si son cúbicos
    cubicos = []
    for numero in candidatos:
        suma = sum(int(d)**3 for d in numero)
        if suma == int(numero):
            cubicos.append(int(numero))

    if cubicos:
        cubicos_str = ' '.join(str(n) for n in cubicos)
        total = sum(cubicos)
        return f"{cubicos_str} {total} Lucky"
    else:
        return "Unlucky"


if __name__ == '__main__':
    print(is_sum_of_cubes("aqdf&0#1xyz!22[153(777.777"))      # "0 1 153 154 Lucky"
    print(is_sum_of_cubes("QK29a45[&erui9026315"))            # "Unlucky"
    print(is_sum_of_cubes("000153"))                          # "000 153 153 Lucky"
    print(is_sum_of_cubes("24172410"))                        # "Unlucky"
    print(is_sum_of_cubes("370371407"))                       # "370 371 407 1148 Lucky"
