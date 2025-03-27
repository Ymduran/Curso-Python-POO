from Examen_Parcial_1.Equipo import Equipo
"""
Clase Torneo:

    Atributos:
        _nombre: Nombre del torneo (protegido).
        _equipos: Lista de equipos en el torneo (protegido).
    Métodos:
        __init__(nombre: str, *equipos: Tuple[Equipo]): Constructor para inicializar los atributos.
        nombre: Mét0do de acceso para obtener y modificar el nombre del torneo. Nota: No se requiere métodos de acceso para _equipos.
        agregar_equipos(*equipos: Tuple[Equipo]): Mét0do para agregar múltiples equipos.
        remover_equipos(*equipos: Tuple[Equipo]): Mét0do para remover múltiples equipos.
        mostrar_equipos(): Mét0do para mostrar la lista de equipos.
        generar_rol(): Mét0do para generar un rol de partidos estilo "todos contra todos" organizado por jornadas, en donde se incluyen a todos los equipos del torneo.
        __str__(): Mét0do para mostrar la información del torneo.
"""



class Torneo:
    def __init__(self, nombre: str, equipos: list[Equipo]):
        self._nombre = nombre
        self._equipos = [Equipo]

    def agregar_equipos(self, *equipos: tuple[Equipo]) -> None:
        pass

    def remover_equipos(self, *equipos: tuple[Equipo]):
        pass

    def mostrar_equipos(self) -> None:
        pass

    def generar_rol(self) -> None:
        pass

    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value


    @property
    def equipos(self) -> tuple[Equipo]:
        return self._equipos
    @nombre.setter
    def nombre(self, value: tuple):
        self._nombre = value


    def __str__(self) -> str:
        return f"Nombre Torneo = {self.nombre} | Equipos = {self._equipos}"