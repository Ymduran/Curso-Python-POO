"""
Torneo.py
"""

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
    def __init__(self, nombre: str, *equipos: Equipo):
        self._nombre = nombre
        self._equipos = list(equipos)  # Se almacena como lista

    def agregar_equipos(self, *equipos: Equipo) -> None:
        for equipo in equipos:
            if equipo not in self._equipos:
                self._equipos.append(equipo)
                print(f"Se agregó equipo {equipo.nombre}")


    def remover_equipos(self, *equipos: Equipo):
        for equipo in equipos:
            if equipo in self._equipos:
                self._equipos.remove(equipo)

    def mostrar_equipos(self) -> None:
        """
        Muestra la lista de equipos en el torneo
        """
        i=0
        print(f"Equipos en el torneo {self._nombre}:")
        for equipo in self._equipos:
            print(f"[{i}] - {equipo.nombre}")
            i+=1

    def generar_rol(self) -> None:
        """
        Genera un rol de partidos 'todos contra todos' organizado en jornadas
        """
        l = 1
        if len(self._equipos) < 2:
            print("No hay suficientes equipos para generar un rol de partidos.")
            return

        jornadas = []
        equipos = self._equipos.copy()


        num_jornadas = len(equipos) - 1
        for i in range(num_jornadas):
            partidos = []
            for j in range(len(equipos) // 2):
                partidos.append((equipos[j], equipos[-(j + 1)]))
            jornadas.append(partidos)
            equipos.insert(1, equipos.pop())  # Rotar equipos

        # Mostrar jornadas
        for i, jornada in enumerate(jornadas, start=1):
            print(f"Jornada {i}:")
            for partido in jornada:
                print(f" {l}- {partido[0].nombre} vs {partido[1].nombre}")
                l+=1
            print()
            l = 1

    def __str__(self) -> str:
        equipos_str = ", ".join(str(equipo) for equipo in self._equipos)
        return f"Nombre del Torneo: {self._nombre} | Equipos: {equipos_str}"

    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self._nombre = nuevo_nombre
    @property
    def equipos(self) -> list[Equipo]:
        """
        Regresará una copia de la lista de equipos para evitar modificaciones externas no controladas
        """
        return self._equipos[:]