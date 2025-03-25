from Clases_y_objetos.Ej2_scoreboard import Scoreboard

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 25 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Ej2_Window                                           * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
"""
    Atributos:
        _title: Título de la ventana (protegido).
        _width: Ancho de la ventana (protegido).
        _height: Alto de la ventana (protegido).
        _scoreboard: Instancia de Scoreboard asociada a la ventana (protegido).
    Métodos:
        __init__(): Constructor para inicializar la ventana con un scoreboard.
        Métodos de acceso: Permiten acceder y modificar los atributos.
        draw_scoreboard(): Llama al método draw del scoreboard para mostrarlo en la ventana.
        update_score(): Actualiza la puntuación del scoreboard y lo redibuja.
        __str__(): Devuelve una representación en cadena del objeto.
"""
class Windows:
    def __init__(self, title: str, width: int, height: int, scoreboard: Scoreboard)-> None:
        self._title = title
        self._width = width
        self._height = height
        self.scoreboard = scoreboard

    def draw_scoreboard(self) -> None:
        pass
    #Mét0do property
    @property
    def title(self) -> int:
        self._title = title
    # Mét0do getter
    @title.getter
    def title(self, _title):
        self._title = title

    # Mét0do property
    @property
    def width(self) -> int:
        self._width = width
    # Mét0do getter
    @width.getter
    def title(self, _width):
        self._width = width

    # Mét0do property
    @property
    def height(self) -> int:
        self._height = height
    # Mét0do getter
    @width.getter
    def title(self, _height):
        self._height = height

    # Mét0do property
    @property
    def height(self) -> int:
        self._scoreboard = scoreboard
    # Mét0do getter
    @width.getter
    def title(self, _scoreboard):
        self._scoreboard = scoreboard







