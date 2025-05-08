print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Eliminar signos de exclamación de una cadena                     * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Escriba una función que elimine todos los signos de exclamación (!) de una cadena dada.

Ejemplo:
Entrada: "¡Hola mundo!"
Salida: "Hola mundo"

Entrada: "Python es increíble!!!"
Salida: "Python es increíble"
"""

def remove_exclamation_marks(s):
    """
    Elimina todos los signos de exclamación de la cadena.

    Parámetro:
    s (str): Cadena original.

    Retorna:
    str: Cadena sin signos de exclamación.
    """
    nueva_cadena = ""
    
    for letra in s:
        if letra != "!":
            nueva_cadena += letra

    return nueva_cadena


if __name__ == '__main__':
    print(remove_exclamation_marks("¡Hola mundo!"))               # ¡Hola mundo
    print(remove_exclamation_marks("Python es increíble!!!"))     # Python es increíble
    print(remove_exclamation_marks("Nada que borrar"))            # Nada que borrar
