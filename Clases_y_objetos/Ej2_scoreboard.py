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
    def __init__(self, points: int, text_color: tuple(int,int,int), font: str, size: float):
        self._points = points
        self._text_color = tuple()
        self._font = font
        self._size = size

    def __str__(self):
        return f"points = {self.points} || text color = {self.text_color} || font = {self.font} || size = {size}"

    def draw(self) -> str:
        pass





        #Mét0do property
        @property
        def points(self)->int:
            self._points = points
        #Mét0do getter
        @points.getter
        def points(self, _points):
            self._points = points

        @property
        def text_color(self) -> tuple():
            self._text_color = tuple()
        @text_color.getter
        def text_color(self, _text_color):
            self._text_color = tuple()

        @property
        def font(self) -> int:
            self._font = font
        # Mét0do getter
        @font.getter
        def font(self, _font):
            self._font = font

        @property
        def size(self) -> int:
            self._size= font
        # Mét0do getter
        @size.getter
        def points(self, _size):
            self._size = size




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






