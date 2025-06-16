print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 12 de junio del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Validar si una cadena es alfanumérica                            * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Instrucciones:
Crear una función llamada alphanumeric que determine si una cadena cumple con:
1. Tener al menos un carácter (no puede estar vacía).
2. Solo contener letras (mayúsculas o minúsculas) o números (0-9).
3. No permitir espacios, guiones bajos, ni símbolos especiales.

La entrada nunca será None o nula, por lo que no es necesario validar eso.
"""

def alphanumeric(password: str) -> bool:
    """
    Verifica si la cadena es alfanumérica:
    - Debe tener al menos un carácter.
    - Todos los caracteres deben ser letras o dígitos.
    
    :param password: Cadena de texto a validar.
    :return: True si es alfanumérica, False en caso contrario.
    """
    if len(password) == 0:
        return False

    for caracter in password:
        # Si el carácter no es letra ni número, retorna False
        if not caracter.isalnum():
            return False

    return True


if __name__ == '__main__':
    print(alphanumeric("abc123"))     # True
    print(alphanumeric("AbC098"))     # True
    print(alphanumeric("abc 123"))    # False (espacio)
    print(alphanumeric("abc_123"))    # False (guion bajo)
    print(alphanumeric("123!"))       # False (signo de exclamación)
    print(alphanumeric(""))           # False (vacía)
    print(alphanumeric("ABC"))        # True
    print(alphanumeric("98765"))      # True
    print(alphanumeric("a"))          # True
    print(alphanumeric(" "))          # False
