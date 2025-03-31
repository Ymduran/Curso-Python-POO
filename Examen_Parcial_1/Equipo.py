
from Examen_Parcial_1.Jugador import Jugador

"""
Clase Equipo:

    Atributos:
        id: Contador de ID único para los equipos (atributo de clase).
        _id_equipo: ID único del equipo (protegido).
        _nombre: Nombre del equipo (protegido).
        _jugadores: Lista de jugadores en el equipo (protegido).
    Métodos:
        __init__(nombre: str, *jugadores: Tuple[Jugador]): Constructor para inicializar los atributos.
        id_equipo, nombre: Métodos de acceso para obtener y modificar los atributos.
            Nota 1: el atributo _id_equipo es únicamente de lectura ({readOnly}), es decir, se tiene un método de acceso getter, pero no un setter.
            Nota 2: No se requiere métodos de acceso para id y _jugadores.
        agregar_jugadores(*jugadores: Tuple[Jugador]): Mét0do para agregar múltiples jugadores.
        remover_jugadores(*jugadores: Tuple[Jugador]): Mét0do para remover múltiples jugadores.
        mostrar_jugadores(): Mét0do para mostrar la lista de jugadores.
        total_goles(): Mét0do para calcular el total de goles anotados por todos los jugadores del equipo.
        __str__(): Mét0do para mostrar la información del equipo.
"""



class Equipo:
    # Atributo de clase
    id_equipo = 1  # Se inicializa en 1
    def __init__(self, nombre: str, *jugadores: tuple[Jugador], id_equipo: int):
        self._nombre = nombre
        self._id_equipo = id_equipo
        self._jugadores = [Jugador]


    def agregar_jugadores(self, *jugadores: tuple[Jugador]) -> None:
        pass

    def remover_jugadores(self, *jugadores: tuple[Jugador]) -> None:
        pass

    def mostrar_jugadores(self) -> None:
        pass

    def total_goles(self) -> None:
        pass

    def __str__(self) -> str:
        return f"Equipo id = {self.id_equipo} | Nombre equipo = {self._nombre} \n Jugadores: {self._jugadores}"




