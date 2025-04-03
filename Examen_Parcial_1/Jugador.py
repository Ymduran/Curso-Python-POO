
"""
class Torneo:
    def __init__(self, nombre: str, equipos: list[Equipo]):

"""

class Jugador:
    """
    Atributos:
        _nombre: Nombre del jugador (protegido).
        _numero: Número del jugador (protegido).
        _goles: Cantidad de goles anotados por el jugador (protegido).
    Métodos:
        __init__(nombre: str, numero: int, goles: int = 0): Constructor para inicializar los atributos.
        nombre, numero, goles: Métodos de acceso para obtener y modificar los atributos.
        anotar_goles(no_goles: int): Mét0do para incrementar la cantidad de goles anotados.
        __str__(): Mét0do para mostrar la información del jugador.
    """

    def __init__(self, nombre: str =" ", numero: int = 0, goles: int = 0):
        self._nombre = nombre
        self._numero = numero
        self._goles = goles


    def anotar_goles(self, no_goles: int) -> None:
        """
        Mét0do para sumar goles
        :param no_goles: Goles a meter, que posteriormente se sumará a un total de goles.
        :return:
        """
        self._goles += no_goles

    def __str__(self) -> str:
        return f"Jugador: {self._nombre} | Número: {self._numero} | Goles: {self._goles}"

    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value

    @property
    def numero(self) -> int:
        return self._numero
    @numero.setter
    def numero(self, value: int):
        self._numero = value

    @property
    def goles(self) -> int:
        return self._goles
    @goles.setter
    def goles(self, value: int):
        self._goles = value



































