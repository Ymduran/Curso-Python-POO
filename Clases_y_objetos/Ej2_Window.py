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
        
    Relación entre Clases:
        La clase Windows tiene una relación de agregación con la clase Scoreboard. Esto significa que la ventana contiene un scoreboard, pero el scoreboard puede existir independientemente de la ventana.



"""


class Window:
    def __init__(self, title: str = "Nueva Ventana", width: int = 800, height: int = 600,
                 scoreboard: Scoreboard = None) -> None:
        self._title = title
        self._width = width
        self._height = height
        self._scoreboard = scoreboard if scoreboard else Scoreboard()

    def draw_scoreboard(self) -> None:
        """Dibuja el scoreboard en la ventana."""
        print(f"Dibujando scoreboard en la ventana '{self._title}'...")
        self._scoreboard.draw()

    def update_score(self, new_score: int) -> None:
        """Actualiza la puntuación del scoreboard y lo redibuja."""
        print(f"Actualizando puntuación a {new_score} en '{self._title}'...")
        self._scoreboard.points = new_score
        self.draw_scoreboard()

    def __str__(self) -> str:
        return f"Window(title='{self._title}', width={self._width}, height={self._height}, scoreboard={self._scoreboard})"

    # Métodos property y setter para los atributos

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if isinstance(value, str) and value.strip():
            self._title = value
        else:
            raise ValueError("El título debe ser una cadena de texto no vacía.")

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        if isinstance(value, int) and value > 0:
            self._width = value
        else:
            raise ValueError("El ancho debe ser un entero positivo.")

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        if isinstance(value, int) and value > 0:
            self._height = value
        else:
            raise ValueError("La altura debe ser un entero positivo.")

    @property
    def scoreboard(self) -> Scoreboard:
        return self._scoreboard

    @scoreboard.setter
    def scoreboard(self, value: Scoreboard) -> None:
        if isinstance(value, Scoreboard):
            self._scoreboard = value
        else:
            raise ValueError("El scoreboard debe ser una instancia de la clase Scoreboard.")




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
    def __init__(self, title: str = "Nueva Ventana", width: int = 800, height: int = 600, scoreboard: Scoreboard = None) -> None:
        self._title = title
        self._width = width
        self._height = height
        self._scoreboard = scoreboard if scoreboard else Scoreboard()

    def draw_scoreboard(self) -> None:
        """Dibuja el scoreboard en la ventana."""
        print(f"Dibujando scoreboard en la ventana '{self._title}'...")
        self._scoreboard.draw()

    def update_score(self, new_score: int) -> None:
        """Actualiza la puntuación del scoreboard y lo redibuja."""
        print(f"Actualizando puntuación a {new_score} en '{self._title}'...")
        self._scoreboard.points = new_score
        self.draw_scoreboard()

    def __str__(self) -> str:
        return f"Window(title='{self._title}', width={self._width}, height={self._height}, scoreboard={self._scoreboard})"

    # Métodos property y setter para los atributos
    
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if isinstance(value, str) and value.strip():
            self._title = value
        else:
            raise ValueError("El título debe ser una cadena de texto no vacía.")

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        if isinstance(value, int) and value > 0:
            self._width = value
        else:
            raise ValueError("El ancho debe ser un entero positivo.")

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        if isinstance(value, int) and value > 0:
            self._height = value
        else:
            raise ValueError("La altura debe ser un entero positivo.")

    @property
    def scoreboard(self) -> Scoreboard:
        return self._scoreboard

    @scoreboard.setter
    def scoreboard(self, value: Scoreboard) -> None:
        if isinstance(value, Scoreboard):
            self._scoreboard = value
        else:
            raise ValueError("El scoreboard debe ser una instancia de la clase Scoreboard.")


if __name__ == "__main__":
    print("  -- Se crean objetos de la clase Window.")

    print("\nSe crea una ventana con valores predeterminados:")
    ventana1 = Window()
    print(f"ventana1 = {ventana1}")

    print("\nSe crea otra ventana con valores personalizados:")
    marcador = Scoreboard(points=25, text_color=(255, 0, 0), font="Verdana", size=20)
    ventana2 = Window("Pantalla de Juego", 1024, 768, marcador)
    print(f"ventana2 = {ventana2}")

    print("\nSe prueba el método draw_scoreboard() en ambas ventanas:")
    ventana1.draw_scoreboard()
    ventana2.draw_scoreboard()

    print("\nSe prueba el método update_score() en la segunda ventana:")
    ventana2.update_score(50)







