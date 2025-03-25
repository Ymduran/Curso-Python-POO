print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 13 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Ejercicio 2 Ej2_Scoreboard                                       * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")

"""
Se necesita desarrollar un sistema que permita gestionar y visualizar un scoreboard (puntuación) dentro de una ventana gráfica. 
El sistema debe cumplir con los siguientes requisitos:
1. Scoreboard:
    - Debe almacenar y gestionar la puntuación actual.
    - Debe permitir actualizar la posición.
    - Debe ser capaz de dibujarse en pantalla con un formato específico.

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
    def __init__(self, points: int = 0, text_color: tuple = (255, 255, 255), font: str = "Arial", size: int = 12):
        self._points = points
        self._text_color = text_color
        self._font = font
        self._size = size

    def __str__(self):
        return f"points = {self._points} || text color = {self._text_color} || font = {self._font} || size = {self._size}"

    def draw(self):
        print(f"[Scoreboard] {self._font} ({self._size}px) - Puntos: {self._points}, Color: {self._text_color}")

    # Métodos property y getter/setter
    @property
    def points(self) -> int:
        return self._points
    @points.setter
    def points(self, value: int):
            self._points = value


    @property
    def text_color(self) -> tuple:
        return self._text_color
    @text_color.setter
    def text_color(self, value: tuple):
            self._text_color = value


    @property
    def font(self) -> str:
        return self._font
    @font.setter
    def font(self, value: str):
            self._font = value


    @property
    def size(self) -> int:
        return self._size
    @size.setter
    def size(self, value: int):
            self._size = value




if __name__ == "__main__":
    # Se crean objetos de la clase y se imprime.
    print("  -- Se crean objetos de la clase Scoreboard.")

    print()
    print("Se crea un objeto sin argumentos:")
    marcador1 = Scoreboard()
    print(f"marcador1 = {marcador1}")

    print()
    print("Se crea otro objeto con (points, font y text_color) como argumentos por nombre:")
    marcador2 = Scoreboard(10, font="Arial", text_color= (127, 127, 127))
    print(f"marcador2 = {marcador2}")

    print()
    print("Se prueba el método draw() en ambos objetos:")
    marcador1.draw()
    marcador2.draw()






