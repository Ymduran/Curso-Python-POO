print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Crear una clase llamada Ball con un tipo de balón               * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Crear una clase llamada Ball.
Los objetos de tipo Ball deben aceptar un argumento para el tipo de balón al crearse.
Si no se da ningún argumento, el tipo de balón debe ser "regular".
"""

class Ball(object):
    """
    Clase que representa un balón con un tipo específico.
    """
    def __init__(self, tipo="regular"):
        self.ball_type = tipo


if __name__ == '__main__':
    ball1 = Ball()
    ball2 = Ball("super")

    print("El tipo de ball1 es:", ball1.ball_type)  # regular
    print("El tipo de ball2 es:", ball2.ball_type)  # super
