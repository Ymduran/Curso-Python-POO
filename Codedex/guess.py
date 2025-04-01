class Jugador:
    def __init__(self, nombre: str, numero: int, goles: int = 0):
        self._nombre = nombre
        self._numero = numero
        self._goles = goles

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

    def anotar_goles(self, no_goles: int) -> None:
        self._goles += no_goles

    def __str__(self) -> str:
        return f"Jugador: {self._nombre} | Número: {self._numero} | Goles: {self._goles}"


#############

"""
Equipo.py
"""
from Examen_Parcial_1.Jugador import Jugador

class Equipo:
    # Atributo de clase para generar IDs únicos
    id = 1  

    def __init__(self, nombre: str, *jugadores: tuple[Jugador]):
        self._id_equipo = Equipo.id  # Se asigna un ID único al equipo
        Equipo.id += 1  # Se incrementa el ID para el próximo equipo
        self._nombre = nombre
        self._jugadores = list(jugadores)  # Se almacena como lista

    @property
    def id_equipo(self) -> int:
        """Propiedad de solo lectura para el ID del equipo"""
        return self._id_equipo

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self._nombre = nuevo_nombre

    def agregar_jugadores(self, *jugadores: tuple[Jugador]) -> None:
        """Agrega múltiples jugadores al equipo"""
        self._jugadores.extend(jugadores)

    def remover_jugadores(self, *jugadores: tuple[Jugador]) -> None:
        """Elimina jugadores específicos del equipo"""
        for jugador in jugadores:
            if jugador in self._jugadores:
                self._jugadores.remove(jugador)

    def mostrar_jugadores(self) -> None:
        """Muestra la lista de jugadores del equipo"""
        print(f"Jugadores del equipo {self._nombre}:")
        for jugador in self._jugadores:
            print(f" - {jugador}")

    def total_goles(self) -> int:
        """Calcula el total de goles anotados por el equipo"""
        return sum(jugador.goles for jugador in self._jugadores)

    def __str__(self) -> str:
        return f"Equipo ID = {self._id_equipo} | Nombre = {self._nombre} \nJugadores: {', '.join(str(j) for j in self._jugadores)}"


############


"""
Torneo.py
"""

from Examen_Parcial_1.Equipo import Equipo

class Torneo:
    def __init__(self, nombre: str, *equipos: tuple[Equipo]):
        self._nombre = nombre
        self._equipos = list(equipos)  # Se almacena como lista

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self._nombre = nuevo_nombre

    def agregar_equipos(self, *equipos: tuple[Equipo]) -> None:
        """Agrega múltiples equipos al torneo"""
        self._equipos.extend(equipos)

    def remover_equipos(self, *equipos: tuple[Equipo]) -> None:
        """Elimina equipos específicos del torneo"""
        for equipo in equipos:
            if equipo in self._equipos:
                self._equipos.remove(equipo)

    def mostrar_equipos(self) -> None:
        """Muestra la lista de equipos en el torneo"""
        print(f"Equipos en el torneo {self._nombre}:")
        for equipo in self._equipos:
            print(f" - {equipo}")

    def generar_rol(self) -> None:
        """Genera un rol de partidos 'todos contra todos' organizado en jornadas"""
        if len(self._equipos) < 2:
            print("No hay suficientes equipos para generar un rol de partidos.")
            return
        
        jornadas = []
        equipos = self._equipos.copy()
        if len(equipos) % 2:
            equipos.append(None)  # Añadir un equipo ficticio si es impar

        num_jornadas = len(equipos) - 1
        for i in range(num_jornadas):
            partidos = []
            for j in range(len(equipos) // 2):
                if equipos[j] is not None and equipos[-(j+1)] is not None:
                    partidos.append((equipos[j], equipos[-(j+1)]))
            jornadas.append(partidos)
            equipos.insert(1, equipos.pop())  # Rotar equipos

        # Mostrar jornadas
        for i, jornada in enumerate(jornadas, start=1):
            print(f"Jornada {i}:")
            for partido in jornada:
                print(f" - {partido[0]} vs {partido[1]}")
            print()

    def __str__(self) -> str:
        equipos_str = ", ".join(str(equipo) for equipo in self._equipos)
        return f"Nombre del Torneo: {self._nombre} | Equipos: {equipos_str}"



#######

"""
Main.py
"""
from colorama import Fore
from Examen_Parcial_1.Jugador import Jugador
from Examen_Parcial_1.Equipo import Equipo
from Examen_Parcial_1.Torneo import Torneo


# Inicializar listas globales
jugadores = []
equipos = []
torneo = Torneo("Torneo Ejemplo", *equipos)

print(Fore.GREEN+ "████████╗ ██████╗ ██████╗ ███╗   ██╗███████╗ ██████╗     ██████╗ ███████╗   ")
print(Fore.RED+   "╚══██╔══╝██╔═══██╗██╔══██╗████╗  ██║██╔════╝██╔═══██╗    ██╔══██╗██╔════╝    ")
print(Fore.CYAN+  "   ██║   ██║   ██║██████╔╝██╔██╗ ██║█████╗  ██║   ██║    ██║  ██║█████╗      ")
print(Fore.YELLOW+"   ██║   ██║   ██║██╔══██╗██║╚██╗██║██╔══╝  ██║   ██║    ██║  ██║██╔══╝       ")
print(Fore.BLUE+  "   ██║   ╚██████╔╝██║  ██║██║ ╚████║███████╗╚██████╔╝    ██████╔╝███████╗    ")
print(Fore.GREEN+ "   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝     ╚═════╝ ╚══════╝    ")
print(Fore.RED+   " ███████╗██╗   ██╗████████╗██████╗  ██████╗ ██╗ ")
print(Fore.CYAN+  " ██╔════╝██║   ██║╚══██╔══╝██╔══██╗██╔═══██╗██║   ")
print(Fore.YELLOW+" █████╗  ██║   ██║   ██║   ██████╔╝██║   ██║██║ ")
print(Fore.BLUE+  " ██╔══╝  ██║   ██║   ██║   ██╔══██╗██║   ██║██║  ")
print(Fore.GREEN+ " ██║     ╚██████╔╝   ██║   ██████╔╝╚██████╔╝███████╗  ")
print(Fore.RED+   " ╚═╝      ╚═════╝    ╚═╝   ╚═════╝  ╚═════╝ ╚══════╝ 69")


def menu_principal() -> None:
    print("[1].- Crear nuevo jugador.")
    print("[2].- Crear nuevo equipo.")
    print("[3].- Ver lista de jugadores.")
    print("[4].- Ver lista de equipos.")
    print("[5].- Agregar jugadores a algún equipo.")
    print("[6].- Eliminar jugadores de un equipo.")
    print("[7].- Agregar equipos al torneo. ")
    print("[8].- Eliminar equipos del torneo. ")
    print("[9].- Anotar gol(es) a un jugador. ")
    print("[10].- Mostrar número total de goles de los equipos")
    print("[11].- Generar rol de juegos. ")
    print("[0].- Salir. ")

def ver_jugadores():
    if jugadores:
        print("Lista de jugadores:")
        for i, jugador in enumerate(jugadores):
            print(f"[{i}] - {jugador.nombre} (Número: {jugador.numero})")
    else:
        print("No hay jugadores registrados.")

def ver_equipos():
    if equipos:
        print("Lista de equipos:")
        for equipo in equipos:
            print(f"{equipo}")
    else:
        print("No hay equipos registrados.")

if __name__ == '__main__':
    flag = 0
    while flag == 0:
        menu_principal()
        option = int(input("Por favor, ingresa una de las opciones anteriores: "))
        if option == 1:  # Crear jugador
            nombre_jugador = input("Ingrese el nombre del nuevo jugador: ")
            numero_jugador = int(input("Ingresa el número del nuevo jugador: "))
            nuevo_jugador = Jugador(nombre_jugador, numero_jugador)
            jugadores.append(nuevo_jugador)
        elif option == 2:  # Crear equipo
            nombre_equipo = input("Ingrese nombre del equipo a crear: ")
            nuevo_equipo = Equipo(nombre_equipo)
            equipos.append(nuevo_equipo)
        elif option == 3:  # Ver lista de jugadores
            ver_jugadores()
        elif option == 4:  # Ver lista de equipos
            ver_equipos()
        elif option == 5:  # Agregar jugador a equipo
            ver_jugadores()
            indice_jugador = int(input("Seleccione el jugador a agregar al equipo: "))
            ver_equipos()
            indice_equipo = int(input("Seleccione el equipo: "))
            equipo = equipos[indice_equipo]
            jugador = jugadores[indice_jugador]
            equipo.agregar_jugadores(jugador)
        elif option == 6:  # Eliminar jugador de equipo
            ver_equipos()
            indice_equipo = int(input("Seleccione el equipo: "))
            equipo = equipos[indice_equipo]
            equipo.mostrar_jugadores()
            indice_jugador = int(input("Seleccione el jugador a eliminar: "))
            equipo.remover_jugadores(equipo._jugadores[indice_jugador])
        elif option == 7:  # Agregar equipo al torneo
            ver_equipos()
            indice_equipo = int(input("Seleccione el equipo a agregar al torneo: "))
            torneo.agregar_equipos(equipos[indice_equipo])
        elif option == 8:  # Eliminar equipo del torneo
            print(f"Equipos en el torneo: {torneo._equipos}")
            indice_equipo = int(input("Seleccione el equipo a eliminar del torneo: "))
            torneo.remover_equipos(torneo._equipos[indice_equipo])
        elif option == 9:  # Anotar goles
            ver_jugadores()
            indice_jugador = int(input("Seleccione el jugador al que se le anotarán goles: "))
            goles_anotar = int(input("Número de goles a anotar: "))
            jugadores[indice_jugador].anotar_goles(goles_anotar)
        elif option == 10:  # Mostrar goles totales por equipo
            for equipo in equipos:
                print(f"Equipo: {equipo.nombre} - Goles totales: {equipo.total_goles()}")
        elif option == 11:  # Generar rol de juegos
            torneo.generar_rol()
        elif option == 0:  # Salir
            print("Saliendo del programa... ")
            flag = 1



