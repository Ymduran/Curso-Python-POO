print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 13 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Ejercicio 2 Scoreboard                                           * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
"""
Se necesita desarrollar un sistema que permita gestionar y visualizar un scoreboard (puntuación) dentro de una ventana gráfica. 
El sistema debe cumplir con los siguientes requisitos:
1. Scoreboard:
        Debe almacenar y gestionar la puntuación actual,
        Debe permitir actualizar la posición,
        Debe ser capaz de dibujarse en pantalla con un formato específico.
        
        
    Atributos:
        _points: Almacena la puntuación actual (protegido).
        _text_color: Define el color del texto del scoreboard (protegido).
        _font: Especifica la fuente del texto (protegido).
        _size: Define el tamaño del texto (protegido).
        
    Métodos:
        __init__(): Constructor para inicializar el scoreboard.
        Métodos de acceso: Permiten acceder y modificar los atributos.
        draw(): Dibuja el scoreboard en la pantalla.
        __str__(): Devuelve una representación en cadena del objeto.
"""
class Scoreboard:
    def __init__(self, points: int, texto_color: tuple(int,int,int), font: str, size: float):
        self._points = points
        self._text_color = tuple()
        self._font = font
        self._size = size

        #Mét0do property
        @property
        def points(self)->int:
            self._points = points
        #Mét0do getter
        @points.getter
        def points(self, _points):
            self._points = points




