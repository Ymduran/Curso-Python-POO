from Clases_y_objetos.Ej2_scoreboard import Scoreboard

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 25 de marzo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Ej2_Window                                                       * ")
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


class Window:
    def __init__(self, title: str = "Nueva Ventana", width: int = 800, height: int = 600, scoreboard: Scoreboard = Scoreboard()) -> None:
        self._title = title
        self._width = width
        self._height = height
        self._scoreboard = scoreboard




    def draw_scoreboard(self) -> None:
        """
        Dibuja el scoreboard en la ventana.
        :return: No retorna nada
        """
        self._scoreboard.draw()



    def update_score(self, points: int) -> None:
        """
        Función que actualiza el score haciendo una llamada al mét0do setter, es decir, modifica en el acceso y no directamente
        :param points: Como argumento recibirá un nuevo score
        :return: No retorna nada
        """
        print(f"Score = {points}")
        self._scoreboard.points = points
        self.draw_scoreboard()




    def __str__(self) -> str:
        return f"Window(title='{self._title}', width={self._width}, height={self._height}, scoreboard={self._scoreboard})"

    # Métodos property y setter
    
    @property
    def title(self) -> str:
        return self._title
    @title.setter
    def title(self, value: str) -> None:
            self._title = value

    @property
    def width(self) -> int:
        return self._width
    @width.setter
    def width(self, value: int) -> None:
            self._width = value


    @property
    def height(self) -> int:
        return self._height
    @height.setter
    def height(self, value: int) -> None:
            self._height = value


    @property
    def scoreboard(self) -> Scoreboard:
        return self._scoreboard
    @scoreboard.setter
    def scoreboard(self, value: Scoreboard) -> None:
            self._scoreboard = value



if __name__ == "__main__":
    # Se crean objetos de la clase Window sin un objeto de la clase Scoreboard creado
    # y se prueban sus métodos.
    print("  -- Se crea un objeto de la clase Window sin un objeto de la clase Scoreboard.")

    buscaminas = Window("Buscaminas", 800, 900)

    print("Se imprime el objeto:")
    print(f"Buscaminas = {buscaminas}")

    print()
    print("Método para dibujar el scoreboard:")
    buscaminas.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    buscaminas.update_score(1)


    # Se crean objetos de ambas clases y se prueban sus métodos.
    print()
    print("  -- Se crea otro objeto de la clase Window, pero ahora con un objeto de la clase Scoreboard.")

    marcador_solitario = Scoreboard(10,(40, 40, 40), "Arial", 40)
    solitario = Window("Solitario", 1_000, 1_000, marcador_solitario)

    print("Se imprimen los objetos:")
    print(f"marcador_solitario = {marcador_solitario}")
    print(f"Solitario = {solitario}")

    print()
    print("Método para dibujar el scoreboard:")
    solitario.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    solitario.update_score(11)


    # Se modifican los atributos mediante los métodos de acceso.
    print()
    print("  -- Se modifican los atributos mediante los métodos de acceso.")

    print("Se tiene la ventana buscaminas:")
    print(f"buscaminas = {buscaminas}")
    print("Se reemplaza el scoreboard utilizando el setter:")
    buscaminas.scoreboard = marcador_solitario
    print(f"buscaminas = {buscaminas}")





