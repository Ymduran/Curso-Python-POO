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
    # Atributo de clase para generar IDs únicos
    id = 1


    def __init__(self, nombre: str, *jugadores: tuple[Jugador]):
        self._id_equipo = Equipo.id  # Se asigna un ID único al equipo
        Equipo.id += 1  # Se incrementa el ID para el próximo equipo
        self._nombre = nombre
        self._jugadores = list(jugadores)  # Se almacena como lista


    def agregar_jugadores(self, *jugadores: tuple[Jugador]) -> None:
        for jugador in jugadores:
            self._jugadores.append(jugador)
            print(f"Se agregó jugador {jugador.nombre} :)")



    def remover_jugadores(self, *jugadores: tuple[Jugador]) -> None:
        """
        Métod0 para remover jugadores, funciona iterando y verifica sí está el jugador en la lista/tupla de jugadores y remueve cuando lo
        encuentre.
        :param jugadores: Puede ser uno o varios jugadores, lo recibe como una tupla.
        :return:
        """

        for jugador in jugadores:
            if jugador in self._jugadores:
                self._jugadores.remove(jugador)

    def mostrar_jugadores(self) -> None:
        """
        Muestra la lista de jugadores del equipo iterando en todos los juagador
        e imprimiendo uno por uno.
        """
        print(f"Jugadores del equipo {self._nombre}:")
        for jugador in self._jugadores:
            print(f" - {jugador}")


    def total_goles(self) -> int:
        """
        Métod0 que calcula el total de goles anotados por el equipo, esto iterando en cada jugador y recuperando sus goles
        para sumarlos al total de goles.
        """
        total_goles = 0
        for jugador in self._jugadores:
            total_goles += jugador.goles
        return total_goles




    def __str__(self) -> str:
        return f"Equipo id = {self.id_equipo} | Nombre equipo = {self._nombre} \n Jugadores: {self._jugadores}"



    #Solo de lectura
    @property
    def id_equipo(self) -> int:
        return self._id_equipo

    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self._nombre = nuevo_nombre


